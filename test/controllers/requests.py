def build_consumer_request_1(faker, random):
    return {
        'name': faker.name(),
        'identification_type': random.choice(["Cédula de ciudadanía", "Cédula de extranjería",
                                              "Tarjeta de identidad", "Pasaporte"]),
        'identification_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
        'contact_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
        'email': faker.email(),
        'address': faker.address(),
        'password': '123456'
    }


def build_consumer_request_2(consumer, faker, random):
    return {
        'name': faker.name(),
        'identification_type': consumer['identification_type'],
        'identification_number': consumer['identification_number'],
        'contact_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
        'email': faker.email(),
        'address': faker.address(),
        'password': '123456'
    }


def build_agent_or_client_request(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': '123456'
    }


def build_company_request(faker):
    return {
        'name': faker.company(),
    }


def build_pcc_request_1(faker):
    return {
        'subject': faker.sentence(),
        'description': faker.paragraph(nb_sentences=20)
    }


def build_pcc_request_2(faker):
    return {
        'subject': faker.sentence(),
        'description': faker.paragraph(nb_sentences=1)
    }


def build_pcc_request_3(faker):
    return {
        'subject': faker.sentence(),
        'description': faker.paragraph(nb_sentences=200)
    }
