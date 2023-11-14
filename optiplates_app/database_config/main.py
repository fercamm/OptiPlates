import db
from optiplates_app.models.models import Comida

if __name__ == "__main__":
    nueva_comida = Comida("Pizza", "Rápida", 300)
    db.guardar_comida(nueva_comida)
