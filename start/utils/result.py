from typing import List, Optional, Any, Dict


class Result:
    # 1. 统一把 None 转成 []，同时给 data 明确的类型提示
    def __init__(
        self,
        success: bool,
        message: str = "",
        data: Optional[List[Any]] = None,
    ):
        # 2. 用 or 一句搞定，不需要两层判断
        self.success: bool = success
        self.message: str = message
        self.data: List[Any] = data or []

    # 3. 返回 dict 时给点类型提示
    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
        }

    # 4. 类方法里同样用 data or [] 即可
    @classmethod
    def ok(
        cls,
        message: str = "",
        data: Optional[List[Any]] = None,
    ) -> "Result":
        return cls(True, message, data)

    @classmethod
    def fail(
        cls,
        message: str = "",
        data: Optional[List[Any]] = None,
    ) -> "Result":
        return cls(False, message, data)