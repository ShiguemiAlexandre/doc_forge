import streamlit as st

from type.contract import Gender, PersonRole, Locador, Locatario, DateContract, TypeContract

st.set_page_config(page_title="Contract Generator", layout="centered")

class Headers:
    def _render(self):
        st.title(
            body=":material/add_notes: Gerar novo contrato",
            # divider=True
        )


class SubHeader:
    def __init__(self):
        self.type_contract = [
            TypeContract.CAUCAO.value.capitalize(),
            TypeContract.SEGURO.value.capitalize(),
            TypeContract.FIADOR.value.capitalize()
        ]

    def _render(self):
        st.selectbox("Tipo do contrato *", options=self.type_contract)
        # TODO CoMEÇO DO CONTRATO E FIM DO CONTRATO NECESSARIO UM RANGE
        st.date_input(f"{DateContract.EMOJI.value} Data do contrato *", value="today", help="Data de início do contrato")

class FormProperty:
    def _render(self):
        st.number_input(
            "Valor do aluguel *",
            min_value=0,
            value=1000,
            step=50,
            format="%d"
        )

        st.text_input("Endereço do imóvel de locação *")

class Body:
    def __init__(self):
        self.LOCATARIO = PersonRole.LOCATARIO.value
        self.LOCADOR = PersonRole.LOCADOR.value

        self.EMOJI_LOCATARIO = Locatario.EMOJI.value
        self.EMOJI_LOCADOR = Locador.EMOJI.value

        self.gender = [
            Gender.MASCULINO.value.capitalize(),
            Gender.FEMININO.value.capitalize()
        ]

        self.form_property = FormProperty()

    def _render(self):
        col1, col2 = st.columns([1, 1])

        col1.subheader(f"{self.EMOJI_LOCATARIO} {self.LOCATARIO.capitalize()}", divider=True)
        col1.text_input("Nome *", help="Nome completo do {}".format(self.LOCATARIO))
        col1.text_input("CPF *", help="CPF do {}".format(self.LOCATARIO))
        col1.text_input("RG *", help="RG do {}".format(self.LOCATARIO))
        col1.text_input("Email *", help="Email do {}".format(self.LOCATARIO))
        col1.text_input("Endereço de residência *", help="Endereço {}".format(self.LOCATARIO))

        col1.selectbox("Selecione o genêro *", options=self.gender, key="gender locatario")

        col2.subheader(f"{self.EMOJI_LOCADOR} {self.LOCADOR.capitalize()}", divider=True)
        col2.text_input("Nome *", help="Nome completo do {}".format(self.LOCADOR))
        col2.text_input("CPF *", help="CPF do {}".format(self.LOCADOR))
        col2.text_input("RG *", help="RG do {}".format(self.LOCADOR))
        col2.text_input("Email *", help="Email do {}".format(self.LOCADOR))
        col2.text_input("Endereço de residência *", help="Endereço {}".format(self.LOCADOR))

        col2.selectbox("Selecione o genêro *", options=self.gender, key="gender locador")

        st.subheader("Formulário da propriedade", divider=True)
        self.form_property._render()

class Footer:
    def _render(self):
        st.button("Gerar")


class ContractCreationPage:
    def __init__(self):
        self.headers = Headers()
        self.sub_headers = SubHeader()
        self.body = Body()
        self.footer = Footer()

    def render(self):
        self.headers._render()

        self.sub_headers._render()

        self.body._render()

        self.footer._render()