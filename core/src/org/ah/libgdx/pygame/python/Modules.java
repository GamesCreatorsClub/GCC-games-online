package org.ah.libgdx.pygame.python;

import org.ah.libgdx.pygame.modules.pygame.PyGameModule;
import org.ah.python.interpreter.GlobalScope;

public class Modules {

    public static void init() {
        GlobalScope.reset();

        GlobalScope.MODULES.put("pygame", PyGameModule.PYGAME_MODULE);
    }

}
