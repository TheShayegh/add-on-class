from abc import ABC, abstractmethod

class CRI(ABC):
    def __init__(
        self,
        overwrite_requirement: bool = False,
        ignore_resetting_error: bool = False,
        auto_construct: bool = True,
        purge_after_construction: bool = True,
        reconstruct: bool = False,
        **requirements
    ) -> None:
        self.__requirements = requirements
        self.__overwrite_requirement = overwrite_requirement
        self.__ignore_resetting_error = ignore_resetting_error
        self.__auto_construct = auto_construct
        if purge_after_construction and reconstruct:
            raise Exception("Can not reconstruct a class after purging it!")
        self.__purge_after_construction = purge_after_construction
        self.__reconstruct = reconstruct
        self.is_constructed = False
            
    @abstractmethod
    def __construct__(self, **requirements) -> None:
        pass
        
    def __are_requirements_met__(self) -> bool:
        if self.is_constructed and not self.__reconstruct:
            return False
        for requirement,value in self.__requirements.items():
            if value is None:
                return False
        return True
        
    def __purge_after_construction__(self) -> None:
        if self.is_constructed:
            del self.__requirements
            del self.__overwrite_requirement
            del self.__ignore_resetting_error
            del self.__auto_construct
            del self.__purge_after_construction
    
    def integrate_requirements(self, ignore_requirements_meeting_error=False) -> None:
        if self.__are_requirements_met__():
            self.__construct__(**self.__requirements)
            self.is_constructed = True
            if self.__purge_after_construction:
                self.__purge_after_construction__()
        elif not ignore_requirements_meeting_error:
            raise Exception("The requirements are not met.")
        
    def meet_requirement(self, requirement: str, value) -> None:
        if self.is_constructed and not self.__reconstruct:
            raise Exception("The object has already been constructed.")
        if self.__requirements[requirement] is None or self.__overwrite_requirement:
            self.__requirements[requirement] = value
        elif not self.__ignore_resetting_error:
            raise Exception("The requirement has already been met.")
        if self.__auto_construct:
            self.integrate_requirements(ignore_requirements_meeting_error=True)