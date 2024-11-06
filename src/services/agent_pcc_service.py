from src.repositories.pcc_repository import PccRepository


class AgentPccService:

    @staticmethod
    def get_pccs_by_agent(agent_id):
        return PccRepository.get_pccs_by_agent_id(agent_id)
