
import ru.ifmo.se.pokemon.*;


public class Litwick extends Pokemon {
    public Litwick(String name, int level) {
        super(name, level);
        setStats(50, 30, 55, 65, 55, 20);
        setType(Type.GHOST, Type.FIRE);
        setMove(new Facade(), new DoubleTeam());
    }
}
