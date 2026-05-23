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
