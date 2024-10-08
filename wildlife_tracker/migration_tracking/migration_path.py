from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self,
                 migration_path_id:int,
                 species: str,
                 start_location: Habitat,
                 destination: Habitat,
                 duration: Optional[int]=None) -> None:
        self.migration_path_id = migration_path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

    def update_migration_path_details(self, **kwargs) -> None:
        pass

    def get_migration_path_details(self) -> dict:
        pass