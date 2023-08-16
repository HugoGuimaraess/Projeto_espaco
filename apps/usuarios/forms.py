from django import forms


class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'EX:João'
            }
        )
    )


    senha = forms.CharField(
        label='Senha',
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua Senha'
            }
        )
    )




class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Digite seu Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex: João'
            }

        )
    )


    senha1=forms.CharField(
        label='Senha',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua Senha'
            }
        )

    )

    senha2 = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua Senha Novamente'
            }
        )
    )


    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite seu e-mail'
            }
        )
    )




    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome=nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços no nome não são permitidos')
            else:
                return nome


    def clean_senha2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')

        if senha1 != senha2:
            raise forms.ValidationError('Senha não podem ser diferentes')

        else:
            return senha2












