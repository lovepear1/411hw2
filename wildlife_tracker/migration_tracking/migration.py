from typing import Any

class Migration:
    
    def __init__(self,
               migration_id:int ,
               current_location: str,
               migration_path_id:str,
               start_date:str,
               status:str) -> None:
        self.migration_id = migration_id
        self.current_location = current_location
        self.migration_path_id = migration_path_id
        self.start_date = start_date
        self.status = status

    def update_migration_details(self, **kwargs: Any) -> None:
        pass

    def get_migration_details(self) -> dict[str, Any]:
        pass