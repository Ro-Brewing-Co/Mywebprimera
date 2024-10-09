from typing import Any

TTL: Any

class RuleCache:
    def __init__(self) -> None: ...
    def get_matched_rule(self, sampling_req, now): ...
    def load_rules(self, rules) -> None: ...
    def load_targets(self, targets_dict) -> None: ...
    @property
    def rules(self): ...
    @rules.setter
    def rules(self, v) -> None: ...
    @property
    def last_updated(self): ...
    @last_updated.setter
    def last_updated(self, v) -> None: ...
