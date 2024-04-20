from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator


class UpdateNodeModel(BaseModel):
    """
    Set of optional fields for updating a node.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

    name: str | None = None
    data: str | None = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if not v:
            raise ValueError("Name cannot be empty")
        return v





