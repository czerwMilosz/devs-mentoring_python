from dataclasses import dataclass, field
from typing import Self

import pandas as pd

@dataclass
class ETLPipeline:
    data: pd.DataFrame | None = field(default=None)

    def extract(self, path:str) -> Self:
        self.data = pd.read_csv(path)
        print(f"Załadowano dane z {path}")
        return self

    def transform(self) -> Self:
        if self.data is None:
            raise ValueError("Brak danych do transformacji")

        self.data.columns = [col.lower() for col in self.data.columns]
        self.data = self.data.dropna()

        print("Transformacja zakonczona")

        return self

    def load(self, output_path:str) -> Self:
        if self.data is None:
            raise ValueError("Brak danych do zapisania")

        self.data.to_csv(output_path, index=False)
        print(f"Dane zostaly zapisane w {output_path}")

        return self

if __name__ == "__main__":
    etl = ETLPipeline().extract("input.csv").transform().load("output.csv")