import os

from PIL import Image
import tempfile
from click.testing import CliRunner

from makejxl import main as conv

tempdir = tempfile.mkdtemp() + os.sep
# tempdir = '/mnt/c/temp/2/'

n1 = tempdir + 'testimage1.jpg'
n2 = tempdir + 'testimage with space.jpg'
n3 = tempdir + 'testimage-with-dash.jpg'
n4 = tempdir + 'testimage.with.dots.jpg'
n5 = tempdir + 'файлик на кириллице.jpg'

r1 = tempdir + 'testimage1.jxl'
r2 = tempdir + 'testimage with space.jxl'
r3 = tempdir + 'testimage-with-dash.jxl'
r4 = tempdir + 'testimage.with.dots.jxl'
r5 = tempdir + 'файлик на кириллице.jxl'

# Generate test images
img = Image.new('RGB', (1024, 1024), color='white')
img.save(n1)
img.save(n2)
img.save(n3)
img.save(n4)
img.save(n5)


def test_1():
    runner = CliRunner()
    result = runner.invoke(conv, tempdir)
    assert result.exit_code == 0


def test_2():
    assert os.path.exists(r1)


def test_3():
    assert os.path.exists(r2)


def test_4():
    assert os.path.exists(r3)


def test_5():
    assert os.path.exists(r4)


def test_6():
    assert os.path.exists(r5)
