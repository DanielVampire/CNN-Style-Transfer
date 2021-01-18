from cx_Freeze import setup, Executable

options = {
    'build.exe':
    {
        'includes':
        [
            'Controller',
            'CNN_Style_Transfer',
            'Content_Loss',
            'Style_Loss',
            'Dialog',
            'ImageProcessor',
            'Normalization',
            'ProgressBarDialog',
            'MainWindowUi',
            'ProgressBarUi',
            'DialogUi'
        ]
     }
}
setup(
    name = 'Neural Style Transfer',
    version ='1.0',
    description = 'Style transfer with neural network and PyQt',
    options = options,
    executables = [Executable("MainWindow.py",
				base='Win32GUI')]
)