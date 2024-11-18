
import ru.ifmo.se.pokemon.*;

public class Darumaka extends Pokemon {
    public Darumaka(String name, int level) {
        super(name, level);
        setStats(70, 90, 45, 15, 45, 50);
        setType(Type.FIRE);
        setMove(new RockSlide(), new FirePunch(), new FlareBlitz());
    }
}


