from pydantic import BaseModel, Field, EmailStr, ConfigDict


user_data = {
    "name": "John Doe",
    "email": "g8rYc@example.com",
    "bio": "I like to code and eat cookies",
    "age": 30,
    # "password": "secret123",
    # "is_active": True
}


class UserSchema(BaseModel):
    email: EmailStr
    name: str
    bio: str | None = Field(default=None, max_length=100)

    model_config = ConfigDict(extra="forbid")

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=150)


user = UserAgeSchema(**user_data)

print(repr(user))


def process_user_data(data):
    pass
