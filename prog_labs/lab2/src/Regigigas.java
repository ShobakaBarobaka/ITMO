
import ru.ifmo.se.pokemon.*;

public class Regigigas extends Pokemon {
    public Regigigas(String name, int level) {
        super(name, level);
        setStats(110, 160, 110, 80, 110, 100);
        setType(Type.NORMAL);
        setMove(new ConfuseRay(), new Bulldoze(), new StoneEdge(), new IcePunch());
    }
}

