package org.ah.libgdx.pygame.python;

import java.io.IOException;

import org.ah.libgdx.pygame.PyGameLibGDX;
import org.ah.python.interpreter.GlobalScope;
import org.ah.python.interpreter.Module;
import org.ah.python.interpreter.ModuleLoader;

public class CreateApplicationUtil {
    public static PyGameLibGDX createApplication(String pythonMainModuleName, ModuleLoader moduleLoader) throws IOException {
        Modules.init();

        GlobalScope.moduleLoader = moduleLoader;

        Module module = moduleLoader.loadModule(pythonMainModuleName);

        int w = 0;
        int h = 0;
        boolean hasSize = false;

//        PyGameModule.PRE_RUN = true;
//        try {
//            module.__call__();
//        } catch (PyGameModule.PyGamePreRunException e) {
//            w = e.getWidth();
//            h = e.getHeight();
//            hasSize = true;
//        } finally {
//            PyGameModule.PRE_RUN = false;
//        }

        PyGameLibGDX application = new PyGameLibGDX(moduleLoader.getPathPrefix(), module);
        if (hasSize) {
            application.setWidth(w);
            application.setHeight(h);
        }
        return application;
    }
}
