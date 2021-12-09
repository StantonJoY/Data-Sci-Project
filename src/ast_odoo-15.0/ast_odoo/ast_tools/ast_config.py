Module(
    body=[
        Import(
            names=[alias(name='configparser', asname='ConfigParser')],
        ),
        Import(
            names=[alias(name='errno', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='optparse', asname=None)],
        ),
        Import(
            names=[alias(name='glob', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='os.path',
            names=[
                alias(name='expandvars', asname=None),
                alias(name='expanduser', asname=None),
                alias(name='abspath', asname=None),
                alias(name='realpath', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[
                alias(name='release', asname=None),
                alias(name='conf', asname=None),
                alias(name='loglevels', asname=None),
            ],
            level=2,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='appdirs', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='passlib.context',
            names=[alias(name='CryptContext', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='crypt_context', ctx=Store())],
            value=Call(
                func=Name(id='CryptContext', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        arg='schemes',
                        value=List(
                            elts=[
                                Constant(value='pbkdf2_sha512', kind=None),
                                Constant(value='plaintext', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ),
                    keyword(
                        arg='deprecated',
                        value=List(
                            elts=[Constant(value='plaintext', kind=None)],
                            ctx=Load(),
                        ),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='MyOption',
            bases=[
                Attribute(
                    value=Name(id='optparse', ctx=Load()),
                    attr='Option',
                    ctx=Load(),
                ),
                Name(id='object', ctx=Load()),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" optparse Option with two additional attributes.\n\n    The list of command line options (getopt.Option) is used to create the\n    list of the configuration file options. When reading the file, and then\n    reading the command line arguments, we don't want optparse.parse results\n    to override the configuration file values. But if we provide default\n    values to optparse, optparse will return them and we can't know if they\n    were really provided by the user or not. A solution is to not use\n    optparse's default attribute, but use a custom one (that will be copied\n    to create the default values of the configuration file).\n\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='opts', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='attrs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='my_default',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attrs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='my_default', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MyOption', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='opts', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='attrs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='DEFAULT_LOG_HANDLER', ctx=Store())],
            value=Constant(value=':INFO', kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='_get_default_datadir',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='home', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='expanduser',
                            ctx=Load(),
                        ),
                        args=[Constant(value='~', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='isdir',
                            ctx=Load(),
                        ),
                        args=[Name(id='home', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='func', ctx=Store())],
                            value=Attribute(
                                value=Name(id='appdirs', ctx=Load()),
                                attr='user_data_dir',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='platform',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='win32', kind=None),
                                            Constant(value='darwin', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='func', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='appdirs', ctx=Load()),
                                        attr='site_data_dir',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='func', ctx=Store())],
                                    value=Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=arg(arg='kwarg', annotation=None, type_comment=None),
                                            defaults=[],
                                        ),
                                        body=BinOp(
                                            left=Constant(value='/var/lib/%s', kind=None),
                                            op=Mod(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='kwarg', ctx=Load()),
                                                        slice=Constant(value='appname', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Name(id='func', ctx=Load()),
                        args=[],
                        keywords=[
                            keyword(
                                arg='appname',
                                value=Attribute(
                                    value=Name(id='release', ctx=Load()),
                                    attr='product_name',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='appauthor',
                                value=Attribute(
                                    value=Name(id='release', ctx=Load()),
                                    attr='author',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_deduplicate_loggers',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='loggers', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Avoid saving multiple logging levels for the same loggers to a save\n    file, that just takes space and the list can potentially grow unbounded\n    if for some odd reason people use :option`--save`` all the time.\n    ', kind=None),
                ),
                Return(
                    value=GeneratorExp(
                        elt=Call(
                            func=Attribute(
                                value=Constant(value='{}:{}', kind=None),
                                attr='format',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='logger', ctx=Load()),
                                Name(id='level', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='logger', ctx=Store()),
                                        Name(id='level', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Call(
                                                        func=Attribute(
                                                            value=Name(id='it', ctx=Load()),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=':', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='it', ctx=Store()),
                                                            iter=Name(id='loggers', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='items',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='configmanager',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Constructor.\n\n        :param fname: a shortcut allowing to instantiate :class:`configmanager`\n                      from Python code without resorting to environment\n                      variable\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='options',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='admin_passwd', kind=None),
                                    Constant(value='csv_internal_sep', kind=None),
                                    Constant(value='publisher_warranty_url', kind=None),
                                    Constant(value='reportgz', kind=None),
                                    Constant(value='root_path', kind=None),
                                ],
                                values=[
                                    Constant(value='admin', kind=None),
                                    Constant(value=',', kind=None),
                                    Constant(value='http://services.openerp.com/publisher-warranty/', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='blacklist_for_save',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='publisher_warranty_url', kind=None),
                                            Constant(value='load_language', kind=None),
                                            Constant(value='root_path', kind=None),
                                            Constant(value='init', kind=None),
                                            Constant(value='save', kind=None),
                                            Constant(value='config', kind=None),
                                            Constant(value='update', kind=None),
                                            Constant(value='stop_after_init', kind=None),
                                            Constant(value='dev_mode', kind=None),
                                            Constant(value='shell_interface', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='casts',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='misc',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='config_file',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='fname', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_LOGLEVELS',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='loglevels', ctx=Load()),
                                                        BinOp(
                                                            left=Constant(value='LOG_%s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='x', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='logging', ctx=Load()),
                                                        Name(id='x', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Tuple(
                                                    elts=[
                                                        Constant(value='CRITICAL', kind=None),
                                                        Constant(value='ERROR', kind=None),
                                                        Constant(value='WARNING', kind=None),
                                                        Constant(value='INFO', kind=None),
                                                        Constant(value='DEBUG', kind=None),
                                                        Constant(value='NOTSET', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='version', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='release', ctx=Load()),
                                            attr='description',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='release', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='parser',
                                    ctx=Store(),
                                ),
                                Name(id='parser', ctx=Store()),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Name(id='version', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='option_class',
                                        value=Name(id='MyOption', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Common options', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-c', kind=None),
                                    Constant(value='--config', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='config', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify alternate config file', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-s', kind=None),
                                    Constant(value='--save', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='save', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='save configuration to ~/.odoorc (or to ~/.openerp_serverrc if it exists)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-i', kind=None),
                                    Constant(value='--init', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='init', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='install one or more modules (comma-separated list, use "all" for all modules), requires -d', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-u', kind=None),
                                    Constant(value='--update', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='update', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='update one or more modules (comma-separated list, use "all" for all modules). Requires -d.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--without-demo', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='without_demo', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='disable loading demo data for modules to be installed (comma-separated, use "all" for all modules). Requires -d and -i. Default is %default', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-P', kind=None),
                                    Constant(value='--import-partial', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='import_partial', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Use this for big data importation, if it crashes you will be able to continue at the current state. Provide a filename to store intermediate importation states.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--pidfile', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='pidfile', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='file where the server pid will be stored', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--addons-path', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='addons_path', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify additional addons paths (separated by commas).', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='callback', kind=None),
                                    ),
                                    keyword(
                                        arg='callback',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_addons_path',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='nargs',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='string', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--upgrade-path', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='upgrade_path', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify an additional upgrade path.', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='callback', kind=None),
                                    ),
                                    keyword(
                                        arg='callback',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_upgrade_path',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='nargs',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='string', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--load', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='server_wide_modules', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Comma-separated list of server-wide modules.', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='base,web', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-D', kind=None),
                                    Constant(value='--data-dir', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='data_dir', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Call(
                                            func=Name(id='_get_default_datadir', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Directory where to store Odoo data', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='HTTP Service Configuration', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--http-interface', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='http_interface', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Listen interface address for HTTP services. Keep empty to listen on all interfaces (0.0.0.0)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-p', kind=None),
                                    Constant(value='--http-port', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='http_port', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=8069, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Listen port for the main HTTP service', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                    keyword(
                                        arg='metavar',
                                        value=Constant(value='PORT', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--longpolling-port', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='longpolling_port', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=8072, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Listen port for the longpolling HTTP service', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                    keyword(
                                        arg='metavar',
                                        value=Constant(value='PORT', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--no-http', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='http_enable', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_false', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Disable the HTTP and Longpolling services entirely', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--proxy-mode', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='proxy_mode', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Activate reverse proxy WSGI wrappers (headers rewriting) Only enable this when running behind a trusted web proxy!', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hidden', ctx=Store())],
                            value=Attribute(
                                value=Name(id='optparse', ctx=Load()),
                                attr='SUPPRESS_HELP',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--xmlrpc-interface', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='http_interface', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Name(id='hidden', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--xmlrpc-port', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='http_port', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Name(id='hidden', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--no-xmlrpc', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='http_enable', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_false', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Name(id='hidden', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Web interface Configuration', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--db-filter', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='dbfilter', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='', kind=None),
                                    ),
                                    keyword(
                                        arg='metavar',
                                        value=Constant(value='REGEXP', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Regular expressions for filtering available databases for Web UI. The expression can use %d (domain) and %h (host) placeholders.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Testing Configuration', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--test-file', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='test_file', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Launch a python test file.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--test-enable', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='callback', kind=None),
                                    ),
                                    keyword(
                                        arg='callback',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_test_enable_callback',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='test_enable', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Enable unit tests.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--test-tags', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='test_tags', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value="Comma-separated list of specs to filter which tests to execute. Enable unit tests if set. A filter spec has the format: [-][tag][/module][:class][.method] The '-' specifies if we want to include or exclude tests matching this spec. The tag will match tags added on a class with a @tagged decorator (all Test classes have 'standard' and 'at_install' tags until explicitly removed, see the decorator documentation). '*' will match all tags. If tag is omitted on include mode, its value is 'standard'. If tag is omitted on exclude mode, its value is '*'. The module, class, and method will respectively match the module name, test class name and test method name. Example: --test-tags :TestClass.test_func,/test_module,external Filtering and executing the tests happens twice: right after each module installation/update and at the end of the modules loading. At each stage tests are filtered by --test-tags specs and additionally by dynamic specs 'at_install' and 'post_install' correspondingly.", kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--screencasts', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='screencasts', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='metavar',
                                        value=Constant(value='DIR', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Screencasts will go in DIR/{db_name}/screencasts.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='temp_tests_dir', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tempfile', ctx=Load()),
                                            attr='gettempdir',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='odoo_tests', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--screenshots', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='screenshots', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Name(id='temp_tests_dir', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='metavar',
                                        value=Constant(value='DIR', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=BinOp(
                                            left=Constant(value='Screenshots will go in DIR/{db_name}/screenshots. Defaults to %s.', kind=None),
                                            op=Mod(),
                                            right=Name(id='temp_tests_dir', ctx=Load()),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Logging Configuration', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--logfile', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='logfile', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='file where the server log will be stored', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--syslog', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='syslog', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Send the log to the syslog server', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-handler', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='append', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Name(id='DEFAULT_LOG_HANDLER', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='metavar',
                                        value=Constant(value='PREFIX:LEVEL', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='setup a handler at LEVEL for a given PREFIX. An empty PREFIX indicates the root logger. This option can be repeated. Example: "odoo.orm:DEBUG" or "werkzeug:CRITICAL" (default: ":INFO")', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-request', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='append_const', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='log_handler', kind=None),
                                    ),
                                    keyword(
                                        arg='const',
                                        value=Constant(value='odoo.http.rpc.request:DEBUG', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='shortcut for --log-handler=odoo.http.rpc.request:DEBUG', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-response', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='append_const', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='log_handler', kind=None),
                                    ),
                                    keyword(
                                        arg='const',
                                        value=Constant(value='odoo.http.rpc.response:DEBUG', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='shortcut for --log-handler=odoo.http.rpc.response:DEBUG', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-web', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='append_const', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='log_handler', kind=None),
                                    ),
                                    keyword(
                                        arg='const',
                                        value=Constant(value='odoo.http:DEBUG', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='shortcut for --log-handler=odoo.http:DEBUG', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-sql', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='append_const', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='log_handler', kind=None),
                                    ),
                                    keyword(
                                        arg='const',
                                        value=Constant(value='odoo.sql_db:DEBUG', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='shortcut for --log-handler=odoo.sql_db:DEBUG', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-db', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='log_db', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Logging database', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-db-level', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='log_db_level', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='warning', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Logging database level', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='levels', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='info', kind=None),
                                    Constant(value='debug_rpc', kind=None),
                                    Constant(value='warn', kind=None),
                                    Constant(value='test', kind=None),
                                    Constant(value='critical', kind=None),
                                    Constant(value='runbot', kind=None),
                                    Constant(value='debug_sql', kind=None),
                                    Constant(value='error', kind=None),
                                    Constant(value='debug', kind=None),
                                    Constant(value='debug_rpc_answer', kind=None),
                                    Constant(value='notset', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--log-level', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='log_level', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='choice', kind=None),
                                    ),
                                    keyword(
                                        arg='choices',
                                        value=Name(id='levels', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='info', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=BinOp(
                                            left=Constant(value='specify the level of the logging. Accepted values: %s.', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[Name(id='levels', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='SMTP Configuration', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--email-from', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='email_from', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the SMTP email address for sending email', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--from-filter', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='from_filter', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify for which email address the SMTP configuration can be used', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--smtp', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='smtp_server', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='localhost', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the SMTP server for sending email', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--smtp-port', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='smtp_port', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=25, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the SMTP port', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--smtp-ssl', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='smtp_ssl', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='if passed, SMTP connections will be encrypted with SSL (STARTTLS)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--smtp-user', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='smtp_user', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the SMTP username for sending email', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--smtp-password', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='smtp_password', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the SMTP password for sending email', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--smtp-ssl-certificate-filename', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='smtp_ssl_certificate_filename', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the SSL certificate used for authentication', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--smtp-ssl-private-key-filename', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='smtp_ssl_private_key_filename', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the SSL private key used for authentication', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Database related options', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-d', kind=None),
                                    Constant(value='--database', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_name', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the database name', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-r', kind=None),
                                    Constant(value='--db_user', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_user', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the database user name', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-w', kind=None),
                                    Constant(value='--db_password', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_password', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the database password', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--pg_path', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='pg_path', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the pg executable path', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--db_host', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_host', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the database host', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--db_port', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_port', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the database port', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--db_sslmode', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_sslmode', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='choice', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='prefer', kind=None),
                                    ),
                                    keyword(
                                        arg='choices',
                                        value=List(
                                            elts=[
                                                Constant(value='disable', kind=None),
                                                Constant(value='allow', kind=None),
                                                Constant(value='prefer', kind=None),
                                                Constant(value='require', kind=None),
                                                Constant(value='verify-ca', kind=None),
                                                Constant(value='verify-full', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the database ssl connection mode (see PostgreSQL documentation)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--db_maxconn', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_maxconn', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=64, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the maximum number of physical connections to PostgreSQL', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--db-template', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_template', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='template0', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify a custom database template to create a new database', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Internationalisation options', kind=None),
                                    Constant(value="Use these options to translate Odoo to another language. See i18n section of the user manual. Option '-d' is mandatory. Option '-l' is mandatory in case of importation", kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--load-language', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='load_language', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specifies the languages for the translations you want to be loaded', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-l', kind=None),
                                    Constant(value='--language', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='language', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify the language of the translation file. Use it with --i18n-export or --i18n-import', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--i18n-export', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='translate_out', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='export all sentences to be translated to a CSV file, a PO file or a TGZ archive and exit', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--i18n-import', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='translate_in', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value="import a CSV or a PO file with translations and exit. The '-l' option is required.", kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--i18n-overwrite', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='overwrite_existing_translations', kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='overwrites existing translation terms on updating a module or importing a CSV or a PO file.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--modules', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='translate_modules', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='specify modules to export. Use in combination with --i18n-export', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='security', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Security-related options', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='security', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--no-database-list', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_false', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='list_db', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Disable the ability to obtain or view the list of databases. Also disable access to the database manager and selector, so be sure to set a proper --database parameter first', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='security', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='optparse', ctx=Load()),
                                    attr='OptionGroup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='parser', ctx=Load()),
                                    Constant(value='Advanced options', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--dev', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='dev_mode', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='string', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Enable developer mode. Param: List of options separated by comma. Options : all, [pudb|wdb|ipdb|pdb], reload, qweb, werkzeug, xml', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--shell-interface', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='shell_interface', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='string', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Specify a preferred REPL to use in shell mode. Supported REPLs are: [ipython|ptpython|bpython|python]', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--stop-after-init', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='stop_after_init', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='stop the server after its initialization', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--osv-memory-count-limit', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='osv_memory_count_limit', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Force a limit on the maximum number of records kept in the virtual osv_memory tables. By default there is no limit.', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--transient-age-limit', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='transient_age_limit', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=1.0, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Time limit (decimal value in hours) records created with a TransientModel (mostly wizard) are kept in the database. Default to 1 hour.', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='float', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--osv-memory-age-limit', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='osv_memory_age_limit', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Deprecated alias to the transient-age-limit option', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='float', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--max-cron-threads', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='max_cron_threads', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=2, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Maximum number of threads processing concurrently cron jobs (default 2).', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='int', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--unaccent', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='unaccent', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Try to enable the unaccent extension when creating new databases.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group', ctx=Load()),
                                    attr='add_option',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--geoip-db', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='geoip_database', kind=None),
                                    ),
                                    keyword(
                                        arg='my_default',
                                        value=Constant(value='/usr/share/GeoIP/GeoLite2-City.mmdb', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Absolute path to the GeoIP database file.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_option_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='posix', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='group', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='optparse', ctx=Load()),
                                            attr='OptionGroup',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='parser', ctx=Load()),
                                            Constant(value='Multiprocessing options', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='add_option',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='--workers', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='dest',
                                                value=Constant(value='workers', kind=None),
                                            ),
                                            keyword(
                                                arg='my_default',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='help',
                                                value=Constant(value='Specify the number of workers, 0 disable prefork mode.', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='int', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='add_option',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='--limit-memory-soft', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='dest',
                                                value=Constant(value='limit_memory_soft', kind=None),
                                            ),
                                            keyword(
                                                arg='my_default',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=2048, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=1024, kind=None),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value=1024, kind=None),
                                                ),
                                            ),
                                            keyword(
                                                arg='help',
                                                value=Constant(value='Maximum allowed virtual memory per worker (in bytes), when reached the worker be reset after the current request (default 2048MiB).', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='int', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='add_option',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='--limit-memory-hard', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='dest',
                                                value=Constant(value='limit_memory_hard', kind=None),
                                            ),
                                            keyword(
                                                arg='my_default',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=2560, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=1024, kind=None),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value=1024, kind=None),
                                                ),
                                            ),
                                            keyword(
                                                arg='help',
                                                value=Constant(value='Maximum allowed virtual memory per worker (in bytes), when reached, any memory allocation will fail (default 2560MiB).', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='int', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='add_option',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='--limit-time-cpu', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='dest',
                                                value=Constant(value='limit_time_cpu', kind=None),
                                            ),
                                            keyword(
                                                arg='my_default',
                                                value=Constant(value=60, kind=None),
                                            ),
                                            keyword(
                                                arg='help',
                                                value=Constant(value='Maximum allowed CPU time per request (default 60).', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='int', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='add_option',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='--limit-time-real', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='dest',
                                                value=Constant(value='limit_time_real', kind=None),
                                            ),
                                            keyword(
                                                arg='my_default',
                                                value=Constant(value=120, kind=None),
                                            ),
                                            keyword(
                                                arg='help',
                                                value=Constant(value='Maximum allowed Real time per request (default 120).', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='int', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='add_option',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='--limit-time-real-cron', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='dest',
                                                value=Constant(value='limit_time_real_cron', kind=None),
                                            ),
                                            keyword(
                                                arg='my_default',
                                                value=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            keyword(
                                                arg='help',
                                                value=Constant(value='Maximum allowed Real time per cron job. (default: --limit-time-real). Set to 0 for no limit. ', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='int', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='add_option',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='--limit-request', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='dest',
                                                value=Constant(value='limit_request', kind=None),
                                            ),
                                            keyword(
                                                arg='my_default',
                                                value=Constant(value=8192, kind=None),
                                            ),
                                            keyword(
                                                arg='help',
                                                value=Constant(value='Maximum number of request to be processed per worker (default 8192).', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='int', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='parser', ctx=Load()),
                                            attr='add_option_group',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='group', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='parser', ctx=Load()),
                                attr='option_groups',
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='option', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='group', ctx=Load()),
                                        attr='option_list',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='option', ctx=Load()),
                                                    attr='dest',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='options',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='options',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Attribute(
                                                                value=Name(id='option', ctx=Load()),
                                                                attr='dest',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='option', ctx=Load()),
                                                        attr='my_default',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='casts',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Attribute(
                                                                value=Name(id='option', ctx=Load()),
                                                                attr='dest',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='option', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_config',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parse_config',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Parse the configuration file (if any) and the command-line\n        arguments.\n\n        This method initializes odoo.tools.config and openerp.conf (the\n        former should be removed in the future) with library-wide\n        configuration values.\n\n        This method must be called before proper usage of this library can be\n        made.\n\n        Typical usage of this method:\n\n            odoo.tools.config.parse_config(sys.argv[1:])\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='opt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_config',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='netsvc',
                                        ctx=Load(),
                                    ),
                                    attr='init_logger',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_warn_deprecated_options',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='modules',
                                            ctx=Load(),
                                        ),
                                        attr='module',
                                        ctx=Load(),
                                    ),
                                    attr='initialize_sys_path',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='opt', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_config',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='args', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='opt', ctx=Store()),
                                        Name(id='args', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='parser',
                                        ctx=Load(),
                                    ),
                                    attr='parse_args',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='die',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='cond', annotation=None, type_comment=None),
                                    arg(arg='msg', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Name(id='cond', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='parser',
                                                        ctx=Load(),
                                                    ),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    Name(id='args', ctx=Load()),
                                    BinOp(
                                        left=Constant(value="unrecognized parameters: '%s'", kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value=' ', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='args', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='opt', ctx=Load()),
                                                        attr='syslog',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='opt', ctx=Load()),
                                                        attr='logfile',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Constant(value='the syslog and logfile options are exclusive', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='translate_in',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='opt', ctx=Load()),
                                                            attr='language',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='opt', ctx=Load()),
                                                            attr='db_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Constant(value='the i18n-import option cannot be used without the language (-l) and the database (-d) options', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='overwrite_existing_translations',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='opt', ctx=Load()),
                                                            attr='translate_in',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='opt', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    Constant(value='the i18n-overwrite option cannot be used without the i18n-import option or without the update option', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='translate_out',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='opt', ctx=Load()),
                                                    attr='db_name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Constant(value='the i18n-export option cannot be used without the database (-d) option', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='opt', ctx=Load()),
                                                    attr='save',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='access',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='opt', ctx=Load()),
                                                            attr='config',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='R_OK',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    BinOp(
                                        left=Constant(value="The config file '%s' selected with -c/--config doesn't exist or is not readable, use -s/--save if you want to generate it", kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='opt', ctx=Load()),
                                            attr='config',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='opt', ctx=Load()),
                                                        attr='osv_memory_age_limit',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='opt', ctx=Load()),
                                                        attr='transient_memory_age_limit',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Constant(value='the osv-memory-count-limit option cannot be used with the transient-age-limit option, please only use the latter.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='nt', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rcfilepath', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='abspath',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='dirname',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='sys', ctx=Load()),
                                                                    attr='argv',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='odoo.conf', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='rcfilepath', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='~/.odoorc', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='old_rcfilepath', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='~/.openerp_serverrc', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='die', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='isfile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='rcfilepath', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='isfile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='old_rcfilepath', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Constant(value="Found '.odoorc' and '.openerp_serverrc' in your path. Please keep only one of them, preferably '.odoorc'.", kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='isfile',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='rcfilepath', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='isfile',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='old_rcfilepath', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='rcfilepath', ctx=Store())],
                                            value=Name(id='old_rcfilepath', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rcfile',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='abspath',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='config_file',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='environ',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ODOO_RC', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='environ',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='OPENERP_SERVER', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='rcfilepath', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='logfile', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='None', kind=None),
                                            Constant(value='False', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='logfile', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='pidfile', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='None', kind=None),
                                            Constant(value='False', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='pidfile', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='test_tags', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='None', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='test_tags', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='server_wide_modules', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='', kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value='False', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='server_wide_modules', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='base,web', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='keys', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='http_interface', kind=None),
                                    Constant(value='http_port', kind=None),
                                    Constant(value='longpolling_port', kind=None),
                                    Constant(value='http_enable', kind=None),
                                    Constant(value='db_name', kind=None),
                                    Constant(value='db_user', kind=None),
                                    Constant(value='db_password', kind=None),
                                    Constant(value='db_host', kind=None),
                                    Constant(value='db_sslmode', kind=None),
                                    Constant(value='db_port', kind=None),
                                    Constant(value='db_template', kind=None),
                                    Constant(value='logfile', kind=None),
                                    Constant(value='pidfile', kind=None),
                                    Constant(value='smtp_port', kind=None),
                                    Constant(value='email_from', kind=None),
                                    Constant(value='smtp_server', kind=None),
                                    Constant(value='smtp_user', kind=None),
                                    Constant(value='smtp_password', kind=None),
                                    Constant(value='from_filter', kind=None),
                                    Constant(value='smtp_ssl_certificate_filename', kind=None),
                                    Constant(value='smtp_ssl_private_key_filename', kind=None),
                                    Constant(value='db_maxconn', kind=None),
                                    Constant(value='import_partial', kind=None),
                                    Constant(value='addons_path', kind=None),
                                    Constant(value='upgrade_path', kind=None),
                                    Constant(value='syslog', kind=None),
                                    Constant(value='without_demo', kind=None),
                                    Constant(value='screencasts', kind=None),
                                    Constant(value='screenshots', kind=None),
                                    Constant(value='dbfilter', kind=None),
                                    Constant(value='log_level', kind=None),
                                    Constant(value='log_db', kind=None),
                                    Constant(value='log_db_level', kind=None),
                                    Constant(value='geoip_database', kind=None),
                                    Constant(value='dev_mode', kind=None),
                                    Constant(value='shell_interface', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='arg', ctx=Store()),
                            iter=Name(id='keys', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='opt', ctx=Load()),
                                                Name(id='arg', ctx=Load()),
                                                Constant(value=None, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='options',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='arg', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='opt', ctx=Load()),
                                                    Name(id='arg', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='str', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='casts',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='optparse', ctx=Load()),
                                                                    attr='Option',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='TYPE_CHECKER',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='options',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='arg', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Subscript(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='optparse', ctx=Load()),
                                                                    attr='Option',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='TYPE_CHECKER',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='casts',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='arg', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='casts',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='arg', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='log_handler', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='log_handler', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='options',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='log_handler', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=',', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='log_handler', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='opt', ctx=Load()),
                                        attr='log_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='keys', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='language', kind=None),
                                    Constant(value='translate_out', kind=None),
                                    Constant(value='translate_in', kind=None),
                                    Constant(value='overwrite_existing_translations', kind=None),
                                    Constant(value='dev_mode', kind=None),
                                    Constant(value='shell_interface', kind=None),
                                    Constant(value='smtp_ssl', kind=None),
                                    Constant(value='load_language', kind=None),
                                    Constant(value='stop_after_init', kind=None),
                                    Constant(value='without_demo', kind=None),
                                    Constant(value='http_enable', kind=None),
                                    Constant(value='syslog', kind=None),
                                    Constant(value='list_db', kind=None),
                                    Constant(value='proxy_mode', kind=None),
                                    Constant(value='test_file', kind=None),
                                    Constant(value='test_tags', kind=None),
                                    Constant(value='osv_memory_count_limit', kind=None),
                                    Constant(value='osv_memory_age_limit', kind=None),
                                    Constant(value='transient_age_limit', kind=None),
                                    Constant(value='max_cron_threads', kind=None),
                                    Constant(value='unaccent', kind=None),
                                    Constant(value='data_dir', kind=None),
                                    Constant(value='server_wide_modules', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='posix_keys', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='workers', kind=None),
                                    Constant(value='limit_memory_hard', kind=None),
                                    Constant(value='limit_memory_soft', kind=None),
                                    Constant(value='limit_time_cpu', kind=None),
                                    Constant(value='limit_time_real', kind=None),
                                    Constant(value='limit_request', kind=None),
                                    Constant(value='limit_time_real_cron', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='posix', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='keys', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='posix_keys', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='dict', ctx=Load()),
                                                    attr='fromkeys',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='posix_keys', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        For(
                            target=Name(id='arg', ctx=Store()),
                            iter=Name(id='keys', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='opt', ctx=Load()),
                                                Name(id='arg', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='options',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='arg', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='opt', ctx=Load()),
                                                    Name(id='arg', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='str', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='casts',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='optparse', ctx=Load()),
                                                                    attr='Option',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='TYPE_CHECKER',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='options',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='arg', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Subscript(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='optparse', ctx=Load()),
                                                                    attr='Option',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='TYPE_CHECKER',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='casts',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='arg', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='casts',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='arg', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='arg', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='root_path', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_normalize',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='dirname',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='__file__', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='..', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='addons_path', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='addons_path', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='None', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default_addons', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='base_addons', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='options',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='root_path', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='addons', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='base_addons', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='default_addons', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='base_addons', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='main_addons', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='abspath',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='options',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='root_path', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='../addons', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='main_addons', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='default_addons', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='main_addons', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='addons_path', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='default_addons', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='addons_path', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_normalize',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='x', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='options',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='addons_path', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='upgrade_path', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='upgrade_path', kind=None),
                                    ctx=Load(),
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Constant(value=',', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        GeneratorExp(
                                            elt=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_normalize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='x', ctx=Load())],
                                                keywords=[],
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='x', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='upgrade_path', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=',', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='init', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='init',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='dict', ctx=Load()),
                                                    attr='fromkeys',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='opt', ctx=Load()),
                                                                attr='init',
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=',', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='demo', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='without_demo', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                body=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='init', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='update', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='update',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='dict', ctx=Load()),
                                                    attr='fromkeys',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='opt', ctx=Load()),
                                                                attr='update',
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=',', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='translate_modules', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='translate_modules',
                                                ctx=Load(),
                                            ),
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='m', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='opt', ctx=Load()),
                                                                    attr='translate_modules',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[Constant(value='all', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='translate_modules', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dev_split', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='opt', ctx=Load()),
                                                attr='dev_mode',
                                                ctx=Load(),
                                            ),
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='s', ctx=Load()),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='s', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='opt', ctx=Load()),
                                                                    attr='dev_mode',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='dev_mode', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='all', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='dev_split', ctx=Load())],
                                            ),
                                            BinOp(
                                                left=Name(id='dev_split', ctx=Load()),
                                                op=Add(),
                                                right=List(
                                                    elts=[
                                                        Constant(value='pdb', kind=None),
                                                        Constant(value='reload', kind=None),
                                                        Constant(value='qweb', kind=None),
                                                        Constant(value='werkzeug', kind=None),
                                                        Constant(value='xml', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Name(id='dev_split', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='opt', ctx=Load()),
                                attr='pg_path',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='pg_path', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='opt', ctx=Load()),
                                        attr='pg_path',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='test_enable', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='test_tags', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='opt', ctx=Load()),
                                attr='save',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='key', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='data_dir', kind=None),
                                    Constant(value='logfile', kind=None),
                                    Constant(value='pidfile', kind=None),
                                    Constant(value='test_file', kind=None),
                                    Constant(value='screencasts', kind=None),
                                    Constant(value='screenshots', kind=None),
                                    Constant(value='pg_path', kind=None),
                                    Constant(value='translate_out', kind=None),
                                    Constant(value='translate_in', kind=None),
                                    Constant(value='geoip_database', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_normalize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='options',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='conf', ctx=Load()),
                                    attr='addons_paths',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='addons_path', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='conf', ctx=Load()),
                                    attr='server_wide_modules',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='m', ctx=Load()),
                                        attr='strip',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='m', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='options',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='server_wide_modules', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=',', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='opt', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_warn_deprecated_options',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='options',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='osv_memory_age_limit', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='warnings', ctx=Load()),
                                            attr='warn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='The osv-memory-age-limit is a deprecated alias to the transient-age-limit option, please use the latter.', kind=None),
                                            Name(id='DeprecationWarning', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='transient_age_limit', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='osv_memory_age_limit', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_addons_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        ImportFrom(
                            module='odoo.modules.module',
                            names=[alias(name='MANIFEST_NAMES', asname=None)],
                            level=0,
                        ),
                        For(
                            target=Name(id='f', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='listdir',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='modpath', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='f', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='isdir',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='modpath', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        FunctionDef(
                                            name='hasfile',
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='filename', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='isfile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='os', ctx=Load()),
                                                                        attr='path',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='modpath', ctx=Load()),
                                                                    Name(id='filename', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            decorator_list=[],
                                            returns=None,
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='hasfile', ctx=Load()),
                                                        args=[Constant(value='__init__.py', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='any', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Call(
                                                                    func=Name(id='hasfile', ctx=Load()),
                                                                    args=[Name(id='mname', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='mname', ctx=Store()),
                                                                        iter=Name(id='MANIFEST_NAMES', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_addons_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='option', annotation=None, type_comment=None),
                            arg(arg='opt', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='parser', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ad_paths', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='value', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='abspath',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='expanduser',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='isdir',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='res', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='optparse', ctx=Load()),
                                                    attr='OptionValueError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='option %s: no such directory: %r', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='opt', ctx=Load()),
                                                                Name(id='res', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_is_addons_path',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='res', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='optparse', ctx=Load()),
                                                    attr='OptionValueError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='option %s: the path %r is not a valid addons directory', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='opt', ctx=Load()),
                                                                Name(id='path', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ad_paths', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='setattr', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='parser', ctx=Load()),
                                        attr='values',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='option', ctx=Load()),
                                        attr='dest',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ad_paths', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_upgrade_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='option', annotation=None, type_comment=None),
                            arg(arg='opt', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='parser', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='upgrade_path', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='value', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_normalize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='isdir',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='res', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='optparse', ctx=Load()),
                                                    attr='OptionValueError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='option %s: no such directory: %r', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='opt', ctx=Load()),
                                                                Name(id='path', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_is_upgrades_path',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='res', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='optparse', ctx=Load()),
                                                    attr='OptionValueError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='option %s: the path %r is not a valid upgrade directory', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='opt', ctx=Load()),
                                                                Name(id='path', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='res', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='upgrade_path', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='upgrade_path', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='setattr', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='parser', ctx=Load()),
                                        attr='values',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='option', ctx=Load()),
                                        attr='dest',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='upgrade_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_upgrades_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='glob', ctx=Load()),
                                                attr='glob',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='res', ctx=Load()),
                                                        JoinedStr(
                                                            values=[
                                                                Constant(value='*/*/', kind=None),
                                                                FormattedValue(
                                                                    value=Name(id='prefix', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value='-*.py', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='prefix', ctx=Store()),
                                                iter=List(
                                                    elts=[
                                                        Constant(value='pre', kind=None),
                                                        Constant(value='post', kind=None),
                                                        Constant(value='end', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_test_enable_callback',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='option', annotation=None, type_comment=None),
                            arg(arg='opt', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='parser', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='parser', ctx=Load()),
                                        attr='values',
                                        ctx=Load(),
                                    ),
                                    attr='test_tags',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='parser', ctx=Load()),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            attr='test_tags',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='+standard', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='load',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='outdated_options_map', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='xmlrpc_port', kind=None),
                                    Constant(value='xmlrpc_interface', kind=None),
                                    Constant(value='xmlrpc', kind=None),
                                ],
                                values=[
                                    Constant(value='http_port', kind=None),
                                    Constant(value='http_interface', kind=None),
                                    Constant(value='http_enable', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ConfigParser', ctx=Load()),
                                    attr='RawConfigParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='p', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='rcfile',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='name', ctx=Store()),
                                            Name(id='value', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='p', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='options', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='outdated_options_map', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='value', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='True', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='value', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='true', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='value', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='False', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='value', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='false', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='options',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='sec', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='p', ctx=Load()),
                                            attr='sections',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='sec', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='options', kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='misc',
                                                        ctx=Load(),
                                                    ),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='sec', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='name', ctx=Store()),
                                                    Name(id='value', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='sec', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='value', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='True', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='value', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='true', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='value', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='False', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='value', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='false', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=Constant(value=False, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='misc',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='sec', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='name', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='ConfigParser', ctx=Load()),
                                        attr='NoSectionError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ConfigParser', ctx=Load()),
                                    attr='RawConfigParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='loglevelnames', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_LOGLEVELS',
                                                        ctx=Load(),
                                                    ),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_LOGLEVELS',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='p', ctx=Load()),
                                    attr='add_section',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='options', kind=None)],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='opt', ctx=Store()),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='opt', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='version', kind=None),
                                                    Constant(value='language', kind=None),
                                                    Constant(value='translate_out', kind=None),
                                                    Constant(value='translate_in', kind=None),
                                                    Constant(value='overwrite_existing_translations', kind=None),
                                                    Constant(value='init', kind=None),
                                                    Constant(value='update', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='opt', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='blacklist_for_save',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='opt', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[Constant(value='log_level', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='options', kind=None),
                                                    Name(id='opt', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='loglevelnames', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='opt', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='opt', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='opt', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='log_handler', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='options', kind=None),
                                                            Name(id='opt', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Constant(value=',', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_deduplicate_loggers', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='options',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Name(id='opt', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='options', kind=None),
                                                            Name(id='opt', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='options',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='opt', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sec', ctx=Store()),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='misc',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='p', ctx=Load()),
                                            attr='add_section',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sec', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='opt', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='misc',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='sec', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='sec', ctx=Load()),
                                                    Name(id='opt', ctx=Load()),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='misc',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='sec', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='opt', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='rc_exists', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rcfile',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='rc_exists', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='os', ctx=Load()),
                                                                    attr='path',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dirname',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='rcfile',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='makedirs',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='dirname',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='rcfile',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='open', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='rcfile',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='w', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='rc_exists', ctx=Load()),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='chmod',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='rcfile',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=384, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='IOError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='sys', ctx=Load()),
                                                                attr='stderr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value="ERROR: couldn't write the config file\n", kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='OSError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sys', ctx=Load()),
                                                        attr='stderr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="ERROR: couldn't create the config directory\n", kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='key', ctx=Load()),
                                    Name(id='default', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pop',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='key', ctx=Load()),
                                    Name(id='default', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_misc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sect', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='misc',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='sect', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='key', ctx=Load()),
                                    Name(id='default', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__setitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='key', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='key', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='options',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Name(id='key', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='casts',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='casts',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='optparse', ctx=Load()),
                                                    attr='Option',
                                                    ctx=Load(),
                                                ),
                                                attr='TYPE_CHECKER',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='optparse', ctx=Load()),
                                                    attr='Option',
                                                    ctx=Load(),
                                                ),
                                                attr='TYPE_CHECKER',
                                                ctx=Load(),
                                            ),
                                            slice=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='casts',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='type',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='casts',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Name(id='key', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='options',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__getitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='options',
                                    ctx=Load(),
                                ),
                                slice=Name(id='key', ctx=Load()),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='addons_data_dir',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='add_dir', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Constant(value='data_dir', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='addons', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='d', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='add_dir', ctx=Load()),
                                    Attribute(
                                        value=Name(id='release', ctx=Load()),
                                        attr='series',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='exists',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='d', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='add_dir', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='makedirs',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='add_dir', ctx=Load()),
                                                            Constant(value=448, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='makedirs',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='d', ctx=Load()),
                                                    Constant(value=320, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='OSError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logging', ctx=Load()),
                                                                    attr='getLogger',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='__name__', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Failed to create addons data dir %s', kind=None),
                                                            Name(id='d', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='d', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='session_dir',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='d', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Constant(value='data_dir', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='sessions', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='makedirs',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='d', ctx=Load()),
                                            Constant(value=448, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='OSError', ctx=Load()),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='errno',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='errno', ctx=Load()),
                                                        attr='EEXIST',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
                                        ),
                                        Assert(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='access',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='d', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='W_OK',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='%s: directory is not writable', kind=None),
                                                op=Mod(),
                                                right=Name(id='d', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='d', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='filestore',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dbname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Constant(value='data_dir', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='filestore', kind=None),
                                    Name(id='dbname', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set_admin_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new_password', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='hash_password', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='crypt_context', ctx=Load()),
                                        Constant(value='hash', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                body=Attribute(
                                    value=Name(id='crypt_context', ctx=Load()),
                                    attr='hash',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Name(id='crypt_context', ctx=Load()),
                                    attr='encrypt',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='options',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='admin_passwd', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='hash_password', ctx=Load()),
                                args=[Name(id='new_password', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='verify_admin_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Verifies the super-admin password, possibly updating the stored hash if needed', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='stored_hash', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='options',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='admin_passwd', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='stored_hash', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='result', ctx=Store()),
                                        Name(id='updated_hash', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='crypt_context', ctx=Load()),
                                    attr='verify_and_update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='password', ctx=Load()),
                                    Name(id='stored_hash', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='result', ctx=Load()),
                            body=[
                                If(
                                    test=Name(id='updated_hash', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='options',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='admin_passwd', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='updated_hash', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_normalize',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='path', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='realpath', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='abspath', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='expanduser', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='expandvars', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='path', ctx=Load()),
                                                                    attr='strip',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='config', ctx=Store())],
            value=Call(
                func=Name(id='configmanager', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
