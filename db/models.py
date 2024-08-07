from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


# Base model for a post
class Post(BaseModel):
    id: Union[str, int]  # ID can be either string or integer
    bodyHTML: str  # HTML content of the post
    title: str  # Title of the post
    URL: str  # URL of the post
    city: str  # City related to the post
    postDate: datetime  # Date when the post was created
    updateDate: datetime  # Date when the post was last updated
    firstImage: Optional[str] = None  # Optional field for the first image URL
    commentCount: int  # Number of comments on the post
# Detailed model for a post extending the base Post model


class PostDetail(Post):
    bodyHTML: str  # HTML content of the post
