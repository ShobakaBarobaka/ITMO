import ru.ifmo.se.pokemon.*;

import static ru.ifmo.se.pokemon.Status.*;

public class Facade extends PhysicalMove {
    public Facade() {
        super(Type.NORMAL, 70, 100);
    }

    @Override
    protected void applyOppDamage(Pokemon p, double damage) {
        Status p_stat = p.getCondition();
        if (p_stat.equals(Status.BURN) || p_stat.equals(Status.POISON) || p_stat.equals(Status.PARALYZE)) {
            super.applyOppDamage(p, damage*2);
        }
        else {
            super.applyOppDamage(p, damage);
        }
    }

    @Override
    protected String describe() {
        return "использует Facade";
    }
}