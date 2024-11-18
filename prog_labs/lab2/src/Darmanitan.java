
import ru.ifmo.se.pokemon.*;

public class Darmanitan extends Darumaka {
    public Darmanitan(String name, int level) {
        super(name, level);
        setStats(105, 140, 55, 30, 55, 95);
        setType(Type.FIRE);
        addMove(new FocusBlast());
    }
}
