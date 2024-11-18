import ru.ifmo.se.pokemon.*;

public class FlareBlitz extends PhysicalMove {
    public FlareBlitz() {
        super(Type.FIRE, 120, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < 0.1){
            Effect.burn(p);
        }
    }

    @Override
    protected String describe() {
        return "использует Flare Blaze";
    }
}