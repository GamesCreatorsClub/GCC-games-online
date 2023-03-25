package org.ah.libgdx.pygame.utils;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;

import com.badlogic.gdx.files.FileHandle;

public class GDXUtil {

    public static String loadString(Reader reader) {
        try {
            StringBuilder res = new StringBuilder();
            char[] buf = new char[10240];
    
            try {
                int r = reader.read(buf);
                while (r > 0) {
                    res.append(buf, 0, r);
                    r = reader.read(buf);
                }
            } finally {
                reader.close();
            }
            
            return res.toString();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static String loadString(FileHandle file) {
        try {
            StringBuilder res = new StringBuilder();
            char[] buf = new char[10240];
    
            InputStreamReader reader = new InputStreamReader(file.read());
            try {
                int r = reader.read(buf);
                while (r > 0) {
                    res.append(buf, 0, r);
                    r = reader.read(buf);
                }
            } finally {
                reader.close();
            }
            
            return res.toString();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}
