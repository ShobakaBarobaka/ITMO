
import ru.ifmo.se.pokemon.Battle;

class Battleground {
    public static void main(String args[]) {
        Battle b = new Battle();

        Regigigas p1 = new Regigigas("Дюдя", 1);
        Darumaka p2 = new Darumaka("Уолтер", 2);
        Darmanitan p3 = new Darmanitan("Донни", 2);
        Litwick p4 = new Litwick("Джефф", 1);
        Lampent p5 = new Lampent("Банни", 3);
        Chandelure p6 = new Chandelure("Хэсус", 1);

        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);

        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);

        b.go();
    }
}