import ru.ifmo.se.pokemon.*;

public class StoneEdge extends PhysicalMove {
    public StoneEdge() {
        super(Type.ROCK, 100, 80);
    }

    @Override
    protected void applyOppDamage(Pokemon p, double damage) {
        if (Math.random() < 0.6) {
            super.applyOppDamage(p, damage*2);
        }
        else {
            super.applyOppDamage(p, damage);
        }
    }

    @Override
    protected String describe() {
        return "использует Stone Edge";
    }
}