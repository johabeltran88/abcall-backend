from src.repositories.company_repository import CompanyRepository


class CompanyService:

    @staticmethod
    def create_company(company):
        return CompanyRepository.create(company)
