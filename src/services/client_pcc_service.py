from src.repositories.client_repository import ClientRepository
from src.repositories.pcc_repository import PccRepository


class ClientPccService:

    @staticmethod
    def get_pccs_by_client(client_id):
        client = ClientRepository.get_by_id(client_id)
        return PccRepository.get_pccs_by_company_id(client.company_id)
