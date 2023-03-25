package org.ah.libgdx.pygame.client;

import org.ah.libgdx.pygame.PyGameLibGDX;
import org.ah.libgdx.pygame.python.CreateApplicationUtil;
import org.ah.python.modules.BuiltInFunctions;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.backends.gwt.GwtApplication;
import com.badlogic.gdx.backends.gwt.GwtApplicationConfiguration;
import com.google.gwt.core.client.GWT;
import com.google.gwt.http.client.Request;
import com.google.gwt.http.client.RequestBuilder;
import com.google.gwt.http.client.RequestCallback;
import com.google.gwt.http.client.RequestException;
import com.google.gwt.http.client.Response;
import com.google.gwt.user.client.Window;

public class HtmlLauncher extends GwtApplication {

//    @Override
//    public GwtApplicationConfiguration getConfig() {
//        return new GwtApplicationConfiguration(480, 320);
//    }
//
//    @Override
//    public ApplicationListener getApplicationListener() {
//        return new PyGameLibGDX();
//    }
    ApplicationListener application;

    String prefix = "games/chris-bot-escape/";

    int width = 1024;
    int height = 768;

    @Override
    public GwtApplicationConfiguration getConfig() {

        GwtApplicationConfiguration cfg = new GwtApplicationConfiguration(width, height);
        return cfg;
    }

    public String getPathPrefix() {
//        String p = GWT.getModuleBaseURL();
//        error("here", "getModuleBaseURL: " + GWT.getModuleBaseURL());
//        error("here", "getHostPageBaseURL: " + GWT.getHostPageBaseURL());
        String p = Window.Location.getHash();
        consoleLog("Window.Location.getHash()=" + p);
        consoleLog("prefix=" + prefix);
        if (p.startsWith("#")) {
            p = p.substring(1);
            if (!p.endsWith("/")) { p = p + "/"; }
        } else {
            p = "";
        }
//        error("here", "" + p);
//        System.out.println(p);
        return p;
    }

    @Override
    public ApplicationListener createApplicationListener () {
        return application;
    }

    protected void callSuperOnModuleLoad() {
        consoleLog("calling super.onModuleLoad()");
        try {
            super.onModuleLoad();
        } catch (Throwable t) {
            consoleLog("Got exception t = " + t.getMessage());
        }
        consoleLog("finished super.onModuleLoad()");
    }

    @Override
    public String getPreloaderBaseURL()
    {
            return GWT.getHostPageBaseURL() + getPathPrefix() + "assets/";
    }


    @Override
    public void onModuleLoad () {
        setLogLevel(LOG_DEBUG);
//        String pythonFileName = "shootingGame/ShootingGame.py";
//        String pythonFileName = "gcc/MazeWithFunctions.py";
//        String pythonFileName = "MazeFinal.py";
//        String pythonFileName = "CaveQuest/maze.py";
//        String pythonFileName = "game-of-circles/maze.py";
//        String pythonFileName = "jonathan-phillips/Maze.py";
//        String pythonFileName = "flappy-bird/Flappy-Bird.py";
//        String pythonFileName = "guns-kills-people!!/JetPack.py";
        String pythonFileName = "game.py";
//        log("Something:", "something x");


        try {
            int i = pythonFileName.indexOf('/');
            final String path = pythonFileName.substring(0, i);
            // final String fileName = pythonFileName.substring(i + 1);
            consoleLog("Loading "+ "assets/" + pythonFileName);
            new RequestBuilder(RequestBuilder.GET, getPathPrefix() + "assets/" + pythonFileName).sendRequest("", new RequestCallback() {

                @Override
                public void onResponseReceived(Request request, Response response) {

                    BuiltInFunctions.printInterface = new BuiltInFunctions.PrintInterface() {
                        @Override
                        public void print(String s) {
                            log("x", s);
                        }
                    };

                    String pythonCode = response.getText();
                    PyGameLibGDX game = CreateApplicationUtil.createApplication(path, pythonCode);
                    width = game.getWidth();
                    height = game.getHeight();
                    consoleLog("Got dimensions [" +  width + "," + height + "]");
                    application = game;

                    consoleLog("callSuperOnModuleLoad");
                    callSuperOnModuleLoad();
                    consoleLog("url=" + Window.Location.getHash());
//                    log("x", "url");
//                    log("x", "url=" + Window.Location.getHash());
                }

                @Override
                public void onError(Request request, Throwable exception) {
                    consoleLog(exception.getMessage());
                    // TODO Auto-generated method stub
                }
            });
        } catch (RequestException e) {
            consoleLog("RequestException " + e.getMessage());
            // TODO Auto-generated catch block
        }
    }
}