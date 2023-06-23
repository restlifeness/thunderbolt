
from sqlalchemy import *
from sqlalchemy.orm import relationship

from .base import ThunderboltModel


class Tag(ThunderboltModel):
    """
    Tag model
    
    The Tag model represents a tag that can be applied to a post.
    
    """
    __tablename__ = 'tag'

    name = Column(String(255), nullable=False, index=True)

    def __repr__(self):
        return f'<Tag {self.name}>'


class Topic(ThunderboltModel):
    """
    Topic model
    
    The Topic model represents a topic that can be discussed in the forum.
    """
    __tablename__ = 'topic'

    symbol = Column(String(3), nullable=False, index=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return f'<Topic {self.title}>'


class Thread(ThunderboltModel):
    """ 
    Thread model
    
    The Thread model represents a thread that can be discussed in the forum.

    """
    __tablename__ = 'thread'

    topic_id = Column(UUID(as_uuid=True), ForeignKey('topic.id'), nullable=False)
    topic = relationship('Topic', backref='threads')

    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return f'<Thread {self.title}>'


class Post(ThunderboltModel):
    """
    Post model
    
    The Post model represents a post that can be discussed in the forum.
    """
    __tablename__ = 'post'

    thread_id = Column(UUID(as_uuid=True), ForeignKey('thread.id'), nullable=False)
    thread = relationship('Thread', backref='posts')

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='posts')

    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.content}>'


class PostTags(ThunderboltModel):
    """
    PostTags model
    
    The PostTags model represents a tag that is applied to a post.
    """
    __tablename__ = 'post_tags'
    
    post_id = Column(UUID(as_uuid=True), ForeignKey('post.id'), nullable=False)
    tag_id = Column(UUID(as_uuid=True), ForeignKey('tag.id'), nullable=False)

    def __repr__(self):
        return f'<PostTags {self.post_id} {self.tag_id}>'
