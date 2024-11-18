import ru.ifmo.se.pokemon.*;

public class FirePunch extends PhysicalMove {
    public FirePunch() {
        super(Type.FIRE, 75, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < 0.1){
            Effect.burn(p);
        }
    }

    @Override
    protected String describe() {
        return "использует Fire Punch";
    }
}