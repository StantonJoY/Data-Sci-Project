Module(
    body=[
        Expr(
            value=Constant(value=' Modules migration handling. ', kind=None),
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='glob', asname=None)],
        ),
        Import(
            names=[alias(name='importlib.util', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='os.path',
            names=[alias(name='join', asname='opj')],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.release', asname='release')],
        ),
        Import(
            names=[alias(name='odoo.upgrade', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools.parse_version',
            names=[alias(name='parse_version', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='load_script',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='path', annotation=None, type_comment=None),
                    arg(arg='module_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='full_path', ctx=Store())],
                    value=IfExp(
                        test=UnaryOp(
                            op=Not(),
                            operand=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='isabs',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        body=Call(
                            func=Name(id='get_resource_path', ctx=Load()),
                            args=[
                                Starred(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='sep',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        orelse=Name(id='path', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='spec', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='importlib', ctx=Load()),
                                attr='util',
                                ctx=Load(),
                            ),
                            attr='spec_from_file_location',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='module_name', ctx=Load()),
                            Name(id='full_path', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='importlib', ctx=Load()),
                                attr='util',
                                ctx=Load(),
                            ),
                            attr='module_from_spec',
                            ctx=Load(),
                        ),
                        args=[Name(id='spec', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='spec', ctx=Load()),
                                attr='loader',
                                ctx=Load(),
                            ),
                            attr='exec_module',
                            ctx=Load(),
                        ),
                        args=[Name(id='module', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='module', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='MigrationManager',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value="\n        This class manage the migration of modules\n        Migrations files must be python files containing a `migrate(cr, installed_version)`\n        function. These files must respect a directory tree structure: A 'migrations' folder\n        which contains a folder by version. Version can be 'module' version or 'server.module'\n        version (in this case, the files will only be processed by this version of the server).\n        Python file names must start by `pre-` or `post-` and will be executed, respectively,\n        before and after the module initialisation. `end-` scripts are run after all modules have\n        been updated.\n        A special folder named `0.0.0` can contain scripts that will be run on any version change.\n        In `pre` stage, `0.0.0` scripts are run first, while in `post` and `end`, they are run last.\n        Example:\n            <moduledir>\n            `-- migrations\n                |-- 1.0\n                |   |-- pre-update_table_x.py\n                |   |-- pre-update_table_y.py\n                |   |-- post-create_plop_records.py\n                |   |-- end-cleanup.py\n                |   `-- README.txt                      # not processed\n                |-- 9.0.1.1                             # processed only on a 9.0 server\n                |   |-- pre-delete_table_z.py\n                |   `-- post-clean-data.py\n                |-- 0.0.0\n                |   `-- end-invariants.py               # processed on all version update\n                `-- foo.py                              # not processed\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='graph', annotation=None, type_comment=None),
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
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cr',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='cr', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='graph',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='graph', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='migrations',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='dict', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_files',
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
                    name='_get_files',
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
                        FunctionDef(
                            name='_get_upgrade_path',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='pkg', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='path', ctx=Store()),
                                    iter=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='upgrade',
                                            ctx=Load(),
                                        ),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='upgrade_path', ctx=Store())],
                                            value=Call(
                                                func=Name(id='opj', ctx=Load()),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Name(id='pkg', ctx=Load()),
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
                                                args=[Name(id='upgrade_path', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=Name(id='upgrade_path', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_scripts',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='path', annotation=None, type_comment=None)],
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
                                            value=Dict(keys=[], values=[]),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=DictComp(
                                        key=Name(id='version', ctx=Load()),
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='glob', ctx=Load()),
                                                attr='glob1',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Name(id='opj', ctx=Load()),
                                                    args=[
                                                        Name(id='path', ctx=Load()),
                                                        Name(id='version', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Constant(value='*.py', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='version', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='listdir',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='path', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='isdir',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='opj', ctx=Load()),
                                                                args=[
                                                                    Name(id='path', ctx=Load()),
                                                                    Name(id='version', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
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
                        For(
                            target=Name(id='pkg', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='graph',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Name(id='hasattr', ctx=Load()),
                                                    args=[
                                                        Name(id='pkg', ctx=Load()),
                                                        Constant(value='update', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='pkg', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='to upgrade', kind=None)],
                                                ),
                                                Compare(
                                                    left=Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='pkg', ctx=Load()),
                                                            Constant(value='load_state', kind=None),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='to upgrade', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='migrations',
                                                ctx=Load(),
                                            ),
                                            slice=Attribute(
                                                value=Name(id='pkg', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='module', kind=None),
                                            Constant(value='module_upgrades', kind=None),
                                            Constant(value='upgrade', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='get_scripts', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='get_resource_path', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='pkg', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='migrations', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='get_scripts', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='get_resource_path', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='pkg', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='upgrades', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='get_scripts', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_get_upgrade_path', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='pkg', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='migrate_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pkg', annotation=None, type_comment=None),
                            arg(arg='stage', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Compare(
                                left=Name(id='stage', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='pre', kind=None),
                                            Constant(value='post', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='stageformat', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='pre', kind=None),
                                    Constant(value='post', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Constant(value='[>%s]', kind=None),
                                    Constant(value='[%s>]', kind=None),
                                    Constant(value='[$%s]', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='state', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='stage', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        Tuple(
                                            elts=[
                                                Constant(value='pre', kind=None),
                                                Constant(value='post', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Attribute(
                                    value=Name(id='pkg', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                orelse=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='pkg', ctx=Load()),
                                        Constant(value='load_state', kind=None),
                                        Constant(value=None, kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Name(id='hasattr', ctx=Load()),
                                                    args=[
                                                        Name(id='pkg', ctx=Load()),
                                                        Constant(value='update', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Compare(
                                                    left=Name(id='state', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='to upgrade', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                    Compare(
                                        left=Name(id='state', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='to install', kind=None)],
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        FunctionDef(
                            name='convert_version',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='version', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='version', ctx=Load()),
                                                attr='count',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[GtE()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='version', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='release', ctx=Load()),
                                                    attr='major_version',
                                                    ctx=Load(),
                                                ),
                                                Name(id='version', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_get_migration_versions',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='pkg', annotation=None, type_comment=None),
                                    arg(arg='stage', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='versions', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            SetComp(
                                                elt=Name(id='ver', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='lv', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='migrations',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Attribute(
                                                                        value=Name(id='pkg', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='values',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='ver', ctx=Store()),
                                                                Name(id='lf', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='lv', ctx=Load()),
                                                                attr='items',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[Name(id='lf', ctx=Load())],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='k', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Call(
                                                        func=Name(id='parse_version', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='convert_version', ctx=Load()),
                                                                args=[Name(id='k', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='0.0.0', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='versions', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='versions', ctx=Load()),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='0.0.0', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='stage', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='pre', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='versions', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value='0.0.0', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='versions', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='0.0.0', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='versions', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_get_migration_files',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='pkg', annotation=None, type_comment=None),
                                    arg(arg='version', annotation=None, type_comment=None),
                                    arg(arg='stage', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' return a list of migration script files\n            ', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='m', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='migrations',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='pkg', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lst', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mapping', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='module', kind=None),
                                            Constant(value='module_upgrades', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='opj', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='pkg', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='migrations', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='opj', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='pkg', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='upgrades', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='path', ctx=Store()),
                                    iter=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='upgrade',
                                            ctx=Load(),
                                        ),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                    body=[
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
                                                args=[
                                                    Call(
                                                        func=Name(id='opj', ctx=Load()),
                                                        args=[
                                                            Name(id='path', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='pkg', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='mapping', ctx=Load()),
                                                            slice=Constant(value='upgrade', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='opj', ctx=Load()),
                                                        args=[
                                                            Name(id='path', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='pkg', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='x', ctx=Store()),
                                    iter=Name(id='mapping', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='version', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='m', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='x', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='f', ctx=Store()),
                                                    iter=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='m', ctx=Load()),
                                                            slice=Name(id='x', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='version', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='f', ctx=Load()),
                                                                        attr='startswith',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='stage', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='-', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            body=[Continue()],
                                                            orelse=[],
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='lst', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='opj', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='mapping', ctx=Load()),
                                                                                slice=Name(id='x', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='version', ctx=Load()),
                                                                            Name(id='f', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
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
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lst', ctx=Load()),
                                            attr='sort',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='lst', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='installed_version', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='pkg', ctx=Load()),
                                            Constant(value='load_version', kind=None),
                                            Attribute(
                                                value=Name(id='pkg', ctx=Load()),
                                                attr='installed_version',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='parsed_installed_version', ctx=Store())],
                            value=Call(
                                func=Name(id='parse_version', ctx=Load()),
                                args=[Name(id='installed_version', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_version', ctx=Store())],
                            value=Call(
                                func=Name(id='parse_version', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='convert_version', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='pkg', ctx=Load()),
                                                    attr='data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='version', kind=None),
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
                        Assign(
                            targets=[Name(id='versions', ctx=Store())],
                            value=Call(
                                func=Name(id='_get_migration_versions', ctx=Load()),
                                args=[
                                    Name(id='pkg', ctx=Load()),
                                    Name(id='stage', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='version', ctx=Store()),
                            iter=Name(id='versions', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='version', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='0.0.0', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='parsed_installed_version', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[Name(id='current_version', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='parsed_installed_version', ctx=Load()),
                                                ops=[
                                                    Lt(),
                                                    LtE(),
                                                ],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='parse_version', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='convert_version', ctx=Load()),
                                                                args=[Name(id='version', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='current_version', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='strfmt', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='addon', kind=None),
                                                    Constant(value='stage', kind=None),
                                                    Constant(value='version', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='pkg', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='stage', ctx=Load()),
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='stageformat', ctx=Load()),
                                                            slice=Name(id='stage', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        op=Mod(),
                                                        right=Name(id='version', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='pyfile', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='_get_migration_files', ctx=Load()),
                                                args=[
                                                    Name(id='pkg', ctx=Load()),
                                                    Name(id='version', ctx=Load()),
                                                    Name(id='stage', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='name', ctx=Store()),
                                                                Name(id='ext', ctx=Store()),
                                                            ],
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
                                                            attr='splitext',
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
                                                                    attr='basename',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='pyfile', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='ext', ctx=Load()),
                                                                attr='lower',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='.py', kind=None)],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='mod', ctx=Store())],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='mod', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='load_script', ctx=Load()),
                                                                args=[
                                                                    Name(id='pyfile', ctx=Load()),
                                                                    Name(id='name', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='module %(addon)s: Running migration %(version)s %(name)s', kind=None),
                                                                        op=Mod(),
                                                                        right=Call(
                                                                            func=Name(id='dict', ctx=Load()),
                                                                            args=[Name(id='strfmt', ctx=Load())],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='name',
                                                                                    value=Attribute(
                                                                                        value=Name(id='mod', ctx=Load()),
                                                                                        attr='__name__',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='migrate', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='mod', ctx=Load()),
                                                                attr='migrate',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='ImportError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='exception',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Constant(value='module %(addon)s: Unable to load %(stage)s-migration file %(file)s', kind=None),
                                                                                op=Mod(),
                                                                                right=Call(
                                                                                    func=Name(id='dict', ctx=Load()),
                                                                                    args=[Name(id='strfmt', ctx=Load())],
                                                                                    keywords=[
                                                                                        keyword(
                                                                                            arg='file',
                                                                                            value=Name(id='pyfile', ctx=Load()),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Raise(exc=None, cause=None),
                                                            ],
                                                        ),
                                                        ExceptHandler(
                                                            type=Name(id='AttributeError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='error',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Constant(value='module %(addon)s: Each %(stage)s-migration file must have a "migrate(cr, installed_version)" function', kind=None),
                                                                                op=Mod(),
                                                                                right=Name(id='strfmt', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='migrate', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='installed_version', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    finalbody=[
                                                        If(
                                                            test=Name(id='mod', ctx=Load()),
                                                            body=[
                                                                Delete(
                                                                    targets=[Name(id='mod', ctx=Del())],
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
