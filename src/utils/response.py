from fastapi import status
from fastapi.responses import JSONResponse
from enum import Enum

class InternalCode(Enum):
	IC_GENERIC_SUCCESS = 2000
	IC_OBJECT_DELETED = 2008
	IC_OBJECT_UPDATED = 2009
	IC_OBJECT_CREATED = 2011
	IC_GENERIC_REDIRECT = 3000
	IC_PERMANENT_REDIRECT = 3011
	IC_GENERIC_CLIENT_ERROR = 4000
	IC_GENERIC_BAD_REQUEST = 4001
	IC_OBJECT_ALREADY_EXISTED = 4009
	IC_GENERIC_UNAUTHORIZED = 4010
	IC_INVALID_CREDENTIALS = 4011
	IC_GENERIC_FORBIDDEN = 4030
	IC_STUDENT_ONLY = 4031
	IC_TEACHER_ONLY = 4032
	IC_ADMIN_ONLY = 4033
	IC_OBJECT_NOT_FOUND = 4041
	IC_GENERIC_SERVER_ERROR = 5000
	IC_GENERIC_NOT_IMPLEMENTED = 5010
	IC_FOR_FUTURE_IMPLEMENTATION = 5011
	IC_DROPPED_SUPPORT = 5019

def APIResponse(status_code: int, internal_code: InternalCode, success: bool = True, body: dict = {}, detail: str = "", headers: dict = {}):
	return JSONResponse(status_code=status_code, 
						headers=headers, 
						content={
							"success": success, 
							"status_code": status_code, 
							"internal_code": internal_code.value, 
							"detail": detail,
							"data":body
						})

