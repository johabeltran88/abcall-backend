import random


def build_consumer_request_1(faker, random):
    return {
        'name': faker.name(),
        'identification_type': random.choice(["Cédula de ciudadanía", "Cédula de extranjería",
                                              "Tarjeta de identidad", "Pasaporte"]),
        'identification_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
        'contact_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
        'email': ''.join([str(random.randint(1, 9)) for _ in range(10)]) + faker.email(),
        'address': faker.address(),
        'password': '123456'
    }


def build_consumer_request_2(consumer, faker, random):
    return {
        'name': faker.name(),
        'identification_type': consumer['identification_type'],
        'identification_number': consumer['identification_number'],
        'contact_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
        'email': ''.join([str(random.randint(1, 9)) for _ in range(10)]) + faker.email(),
        'address': faker.address(),
        'password': '123456'
    }


def build_agent_or_client_request(faker):
    return {
        'name': faker.name(),
        'email': ''.join([str(random.randint(1, 9)) for _ in range(10)]) +faker.email(),
        'password': '123456'
    }


def build_company_request(faker):
    return {
        'name': faker.company(),
    }


def build_pcc_request_1(faker):
    return {
        'subject': faker.sentence(),
        'description': "microchip magnetic embrace Markets encoding blue collaborative Croatia Assurance France Legacy overriding ivory payment Delaware solution-oriented coherent Baht services Denar Garden Distributed sticky edge fresh-thinking Wooden application Avon Dakota Wells Fantastic bandwidth-monitored Balanced France Chief bandwidth portals Rubber customized transmit pink Advanced navigating Practical Games black Berkshire bandwidth drive Cotton Wooden web-readiness Berkshire navigate Cambridgeshire Engineer cross-media wireless definition blue Berkshire Generic Solutions drive SAS Wooden Automotive Won Shirt sky Egyptian 24 Rustic Alabama Fork Implemented digital Soap payment markets optimal communities stable Global synthesize Berkshire deposit Customer online digital Bermuda Global Interface silver Berkshire Tennessee Research Consultant Guilder Buckinghamshire"
    }


def build_pcc_request_2(faker):
    return {
        'subject': faker.sentence(),
        'description': faker.paragraph(nb_sentences=1)
    }


def build_pcc_request_3(faker):
    return {
        'subject': faker.sentence(),
        'description': faker.paragraph(nb_sentences=300)
    }
