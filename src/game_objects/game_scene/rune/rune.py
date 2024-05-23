import pgframework as pgf
from .rune_effects.rune_effect import RuneEffect


class Rune(pgf.GameObject):
    def __init__(self, sprite_file: str, name: str, description: str, activation_time: int, energy_cost: float, activation_effect: RuneEffect, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 16, 16))

        self._name = name
        self._description = description

        self._activation_time = activation_time
        self._energy_cost = energy_cost

        self._activation_effect: RuneEffect = activation_effect
        self._induction_effect: RuneEffect = None  # rune_induction_effect

        self.add_child(pgf.components.sprite2d.Sprite2D(self, sprite_file))

    def get_activation_time(self) -> int:
        return self._activation_time
    
    def get_energy_cost(self) -> int:
        return self._energy_cost

    def get_activation_effect(self) -> RuneEffect:
        return self._activation_effect
    
    def get_induction_effect(self) -> RuneEffect:
        return self._induction_effect
    
    def start(self, combat_controller: 'CombatController', self_agent: 'CombatAgent', other_agent: 'CombatAgent'):
        activation_effect = self.get_activation_effect()
        if activation_effect is not None:
            rune_activation_start_effect = activation_effect.get_combat_start_effect()
            
            if rune_activation_start_effect is not None:
                rune_activation_start_effect.get_callback()(combat_controller, self_agent, other_agent.get_opponent())
        
        induction_effect = self.get_induction_effect()
        if induction_effect is not None:
            rune_induction_start_effect = induction_effect.get_combat_start_effect()

            if rune_induction_start_effect is not None:
                rune_induction_start_effect.get_callback()(combat_controller, self_agent, other_agent.get_opponent())

    def end(self, combat_controller: 'CombatController', self_agent: 'CombatAgent', other_agent: 'CombatAgent'):
        activation_effect = self.get_activation_effect()
        if activation_effect is not None:
            rune_activation_end_effect = activation_effect.get_combat_end_effect()
            
            if rune_activation_end_effect is not None:
                rune_activation_end_effect.get_callback()(combat_controller, self_agent, other_agent.get_opponent())
        
        induction_effect = self.get_induction_effect()
        if induction_effect is not None:
            rune_induction_end_effect = induction_effect.get_combat_end_effect()

            if rune_induction_end_effect is not None:
                rune_induction_end_effect.get_callback()(combat_controller, self_agent, other_agent.get_opponent())

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        description = f'{self._description}<br>'
        description += f'<br>'
        description += f'<color rgb="(197, 152, 70)">Custo de energia: </color>'
        description += f'{self._energy_cost}<br>'
        description += f'<color rgb="(197, 152, 70)">Tempo de ativacao: </color>'
        description += f'{self._activation_time}<br>'

        if self._activation_effect is not None:
            description += f'<color rgb="(197, 152, 70)">Efeito de ativacao: </color>'
            description += f'{self._activation_effect.get_description()}<br>'

        if self._rune_induction_effect is not None:
            description += f'<color rgb="(197, 152, 70)">Efeito de inducao: </color>'
            description += f'{self._rune_induction_effect.get_description()}<br>'

        return description
