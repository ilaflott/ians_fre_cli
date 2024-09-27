''' test "fre catalog" calls '''

from click.testing import CliRunner

from fre import fre

runner = CliRunner()

def test_cli_fre_catalog():
    ''' fre catalog '''
    result = runner.invoke(fre.fre, args=["catalog"])
    assert result.exit_code == 0

def test_cli_fre_catalog_help():
    ''' fre catalog --help '''
    result = runner.invoke(fre.fre, args=["catalog", "--help"])
    assert result.exit_code == 0

def test_cli_fre_catalog_opt_dne():
    ''' fre catalog optionDNE '''
    result = runner.invoke(fre.fre, args=["catalog", "optionDNE"])
    assert result.exit_code == 2

def test_cli_fre_catalog_builder():
    ''' fre catalog builder '''
    result = runner.invoke(fre.fre, args=["catalog", "builder"])
    assert all( [
                  result.exit_code == 1,
                  'Missing: input_path or output_path. Pass it in the config yaml or as command-line option'
                    in result.stdout.split('\n')
                ]
              )

def test_cli_fre_catalog_builder_help():
    ''' fre catalog builder --help '''
    result = runner.invoke(fre.fre, args=["catalog", "builder", "--help"])
    assert result.exit_code == 0