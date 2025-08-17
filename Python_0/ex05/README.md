#Créer un environnement virtuel (recommandé)

python -m venv env
source env/bin/activate


#Installer Flake8 (alias "norminette" Python)

pip install flake8
alias norminette='flake8'

#Pour le rendre permanent

nano ~/.bashrc
alias norminette='flake8'
source ~/.bashrc


si zsh

nano ~/.zshrc
alias norminette='flake8'
source ~/.zshrc
