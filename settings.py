from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    screen_w: int = 1260
    screen_h: int = 720
    screen_bg_color: str = "#ffff00"
    border_color: str = "#eeee00"
    snake_color: str = "#00ff00"
    apple_color: str = "#ff0000"
    sq_size: int = 30  # px
    pula: int = screen_w // sq_size
    screen_sq_y: int = screen_h // sq_size
    fps: int = 5


settings = Settings()
