init python:
    if renpy.android:
        from jnius import autoclass
        TetrisManager = autoclass('org.renpy.android.TetrisManager')
        
        def show_tetris_controls():
            TetrisManager.showTetrisOverlay()
            
        def hide_tetris_controls():
            TetrisManager.hideTetrisOverlay()
    else:
        def show_tetris_controls():
            pass
            
        def hide_tetris_controls():
            pass
    
    def get_android_stockfish_path():
        """
        Returns the path to the executable stockfish binary on Android.
        Should be called before starting the chess engine.
        Returns None if setup fails or not on Android.
        """
        if not renpy.android:
            return None

        try:
            from jnius import autoclass

            PythonSDLActivity = autoclass('org.renpy.android.PythonSDLActivity')
            mActivity = PythonSDLActivity.mActivity

            app_info = mActivity.getApplicationInfo()
            native_lib_dir = app_info.nativeLibraryDir
            stockfish_so = os.path.join(native_lib_dir, "libstockfish.so")
            
            if os.path.exists(stockfish_so):
                return stockfish_so
                
            return None

        except Exception:
            try:
                private_files = os.environ.get("ANDROID_PRIVATE")
                lib_dir = os.path.normpath(os.path.join(private_files, "..", "lib"))
                stockfish_so = os.path.join(lib_dir, "libstockfish.so")
                
                if os.path.exists(stockfish_so):
                    return stockfish_so
            except:
                pass
                
            return None 
