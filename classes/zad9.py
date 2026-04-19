from datetime import datetime



class Tank:
    """Represents a single water tank with capacity and current water volume."""
    def __init__(self, name: str, capacity: float):
        """Initialize tank name, capacity, and starting volume."""

        if name.strip() == "":
            raise ValueError("Tank name cannot be empty")
        if capacity <= 0:
            raise ValueError("Tank capacity cannot be negative")

        self.name = name
        self.capacity = capacity
        self.current_volume: float = 0

    def pour_water(self, volume: float) -> bool:
        """Try to pour water into the tank and return whether it succeeded."""
        if volume <= 0 or self.current_volume + volume > self.capacity:
            return False

        self.current_volume += volume
        return True

    def pour_out_water(self, volume: float) -> bool:
        """Try to pour water out of the tank and return whether it succeeded."""
        if volume <= 0 or self.current_volume < volume:
            return False

        self.current_volume -= volume
        return True

    def __repr__(self):
        """Return a readable string representation of the tank."""
        return f"Tank(name={self.name}, volume={self.current_volume}/{self.capacity})"


class TankEvent:
    """Stores a single tank operation event with execution details."""
    def __init__(self, timestamp, operation_name, tank_name, volume, success, source_tank_name=None):
        """Initialize event data for a tank operation."""
        self.tank_name = tank_name  # target
        self.source_tank_name = source_tank_name  # source
        self.timestamp = timestamp
        self.operation_name = operation_name
        self.volume = volume
        self.success = success # True / False

    def __repr__(self):
        """Return a readable string representation of the event."""
        return (f"\n"
                f"\nTankEvent(time={self.timestamp}, "
                f"\noperation_name='{self.operation_name}', "
                f"\ntarget='{self.tank_name}', "
                f"\nsource='{self.source_tank_name}', "
                f"\nvolume={self.volume}, "
                f"\nsuccess={self.success})")


class TankManager:
    """Manages tanks, executes operations, and stores event history."""
    def __init__(self):
        """Initialize storage for tanks and operation events."""
        self.tanks = {}
        self.events = []

    def add_tank(self, name: str, capacity: float):
        """Create a new tank and add it to the manager."""
        self.tanks[name] = Tank(name, capacity)

    def pour_water(self, tank_name: str, volume: float):
        """Perform a pour-in operation and save its event."""
        tank = self.tanks[tank_name]
        success = tank.pour_water(volume) # True / False
        self.events.append(
            TankEvent(
                tank_name = tank_name,
                source_tank_name = None,
                timestamp = datetime.now(),
                operation_name = "pour_water",
                volume = volume,
                success = success
        ))
        return success

    def pour_out_water(self, tank_name: str, volume: float):
        """Perform a pour-out operation and save its event."""
        tank = self.tanks[tank_name]
        success = tank.pour_out_water(volume)
        self.events.append(
            TankEvent(
                tank_name = tank_name,
                source_tank_name = None,
                timestamp = datetime.now(),
                operation_name = "pour_out_water",
                volume = volume,
                success = success
            )
        )
        return success

    def transfer_water(self, from_tank_name:str, to_tank_name:str, volume: float):
        """Transfer water between tanks and save the transfer event."""
        from_tank = self.tanks[from_tank_name]
        to_tank = self.tanks[to_tank_name]
        success = True

        if (
            volume <= 0
            or from_tank.current_volume < volume
            or to_tank.current_volume + volume > to_tank.capacity
        ):
            success = False
        else:
            from_tank.pour_out_water(volume)
            to_tank.pour_water(volume)

        self.events.append(
            TankEvent(
                tank_name = to_tank_name,            # target
                source_tank_name = from_tank_name,   # source
                timestamp = datetime.now(),
                operation_name = "transfer_water",
                volume = volume,
                success = success
            )
        )
        return success

    def get_tank_with_most_water(self):
        """Return the tank that currently contains the most water."""
        if not self.tanks:
            return []
        return max(self.tanks.values(), key=lambda x: x.current_volume)

    def get_most_filled_tank(self):
        """Return the tank with the highest fill ratio."""
        if not self.tanks:
            return []
        return max(self.tanks.values(), key=lambda x: x.current_volume / x.capacity)

    def get_empty_tank(self):
        """Return a list of tanks that are currently empty."""
        empty_tanks = []
        for tank in self.tanks.values():
            if tank.current_volume == 0:
                empty_tanks.append(tank)
        return empty_tanks

    def get_tanks_with_most_failed_operations(self):
        """Return tank names with the highest number of failed operations."""
        count = {}
        result = []

        for event in self.events:
            if not event.success:
                count[event.tank_name] = count.get(event.tank_name, 0) + 1

        if not count:
            return result # result = []

        max_value = max(count.values())

        for tank_name, count in count.items():
            if count == max_value:
                result.append(tank_name)
        return result

    def get_tanks_with_most_operations_of_type(self, operation_name):
        """Return tank names with the highest number of operations of the given type."""
        count = {}
        result = []
        for event in self.events:
            if event.operation_name == operation_name:
                count[event.tank_name] = count.get(event.tank_name, 0) + 1

        if not count:
            return result   #result = []

        max_value = max(count.values())

        for tank_name, count in count.items():
            if count == max_value:
                result.append(tank_name)
        return result

    def check_state(self, tank_name: str):
        """Recalculate tank volume from successful events and compare it with current state."""
        volume = 0

        for event in self.events:
            if not event.success:
                continue

            if event.operation_name == "pour_water" and event.tank_name == tank_name:
                volume += event.volume

            elif event.operation_name == "pour_out_water" and event.tank_name == tank_name:
                volume -= event.volume

            elif event.operation_name == "transfer_water":
                if event.tank_name == tank_name:
                    volume += event.volume
                elif event.source_tank_name == tank_name:
                    volume -= event.volume

        actual = self.tanks[tank_name].current_volume

        return {
            "calculated": volume,
            "actual": actual,
            "is_consistent": volume == actual
        }

    def __repr__(self):
        """Return a readable string representation of all managed tanks."""
        return "\n".join([str(tank) for tank in self.tanks.values()])


def main():
    """Create sample tanks, run example operations, and print results."""
    tank_manager = TankManager()
    tank_manager.add_tank("tank1", 200)
    tank_manager.add_tank("tank2", 10)
    tank_manager.add_tank("tank3", 20)
    tank_manager.add_tank("tank4", 30)
    tank_manager.add_tank("tank5", 5)
    print(tank_manager.tanks)
    tank_manager.pour_water("tank1", 100)
    tank_manager.pour_water("tank1", 200)
    tank_manager.pour_water("tank1", 250)
    tank_manager.pour_water("tank1", 300)
    tank_manager.pour_out_water("tank1", 20)
    tank_manager.pour_water("tank2", 9)
    tank_manager.transfer_water("tank2", "tank1", 5)
    tank_manager.pour_water("tank5", 10)
    tank_manager.pour_water("tank5", 15)
    tank_manager.pour_water("tank5", 20)
    tank_manager.pour_water("tank5", 3)
    print(f"Tank with most water: {tank_manager.get_tank_with_most_water()}")
    print(f"Most filled tank (by %): {tank_manager.get_most_filled_tank()}")
    print(f"Empty tanks: {tank_manager.get_empty_tank()}")
    print(f"Tanks with most failed operations: "
          f"{tank_manager.get_tanks_with_most_failed_operations()}")
    print(f"Tanks with most 'pour_water' operations: "
        f"{tank_manager.get_tanks_with_most_operations_of_type('pour_water')}")
    print(tank_manager.check_state("tank1"))
    print(tank_manager.events)

if __name__ == "__main__":
    main()