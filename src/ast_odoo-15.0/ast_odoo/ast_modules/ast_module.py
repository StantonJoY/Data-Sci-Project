Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='collections.abc', asname=None)],
        ),
        Import(
            names=[alias(name='importlib', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='pkg_resources', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        ImportFrom(
            module='os.path',
            names=[alias(name='join', asname='opj')],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.tools', asname='tools')],
        ),
        Import(
            names=[alias(name='odoo.release', asname='release')],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='pycompat', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='MANIFEST_NAMES', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='__manifest__.py', kind=None),
                    Constant(value='__openerp__.py', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='README', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='README.rst', kind=None),
                    Constant(value='README.md', kind=None),
                    Constant(value='README.txt', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
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
            name='ad_paths',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='warnings', ctx=Load()),
                            attr='warn',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='"odoo.modules.module.ad_paths" is a deprecated proxy to "odoo.addons.__path__".', kind=None),
                            Name(id='DeprecationWarning', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='stacklevel',
                                value=Constant(value=2, kind=None),
                            ),
                        ],
                    ),
                ),
                Return(
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='addons',
                            ctx=Load(),
                        ),
                        attr='__path__',
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[
                Attribute(
                    value=Name(id='tools', ctx=Load()),
                    attr='lazy',
                    ctx=Load(),
                ),
            ],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='loaded', ctx=Store())],
            value=List(elts=[], ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='AddonsHook',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Makes modules accessible through openerp.addons.* ', kind=None),
                ),
                FunctionDef(
                    name='find_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='name', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='openerp.addons.', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='name', ctx=Load()),
                                                attr='count',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                ],
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
                                            Constant(value='"openerp.addons" is a deprecated alias to "odoo.addons".', kind=None),
                                            Name(id='DeprecationWarning', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='stacklevel',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Return(
                                    value=Name(id='self', ctx=Load()),
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
                    name='load_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
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
                                left=Name(id='name', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='odoo_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^openerp.addons.(\\w+)$', kind=None),
                                    Constant(value='odoo.addons.\\g<1>', kind=None),
                                    Name(id='name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='odoo_module', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='odoo_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='odoo_module', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='odoo_module', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='importlib', ctx=Load()),
                                            attr='import_module',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='odoo_name', ctx=Load())],
                                        keywords=[],
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
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='name', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='odoo_module', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='odoo_module', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='OdooHook',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Makes odoo package also available as openerp ', kind=None),
                ),
                FunctionDef(
                    name='find_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^openerp\\b', kind=None),
                                    Name(id='name', ctx=Load()),
                                ],
                                keywords=[],
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
                                            Constant(value='openerp is a deprecated alias to odoo.', kind=None),
                                            Name(id='DeprecationWarning', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='stacklevel',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Return(
                                    value=Name(id='self', ctx=Load()),
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
                    name='load_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
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
                                left=Name(id='name', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='canonical', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^openerp(.*)', kind=None),
                                    Constant(value='odoo\\g<1>', kind=None),
                                    Name(id='name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='canonical', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mod', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='modules',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='canonical', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='mod', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='importlib', ctx=Load()),
                                            attr='import_module',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='canonical', ctx=Load())],
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
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='name', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='mod', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='modules',
                                    ctx=Load(),
                                ),
                                slice=Name(id='name', ctx=Load()),
                                ctx=Load(),
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
        ClassDef(
            name='UpgradeHook',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Makes the legacy `migrations` package being `odoo.upgrade`', kind=None),
                ),
                FunctionDef(
                    name='find_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^odoo.addons.base.maintenance.migrations\\b', kind=None),
                                    Name(id='name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Name(id='self', ctx=Load()),
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
                    name='load_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
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
                                left=Name(id='name', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='canonical_upgrade', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='name', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='odoo.addons.base.maintenance.migrations', kind=None),
                                    Constant(value='odoo.upgrade', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='canonical_upgrade', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mod', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='modules',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='canonical_upgrade', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='mod', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='importlib', ctx=Load()),
                                            attr='import_module',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='canonical_upgrade', ctx=Load())],
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
                                        value=Name(id='sys', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='name', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='mod', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='modules',
                                    ctx=Load(),
                                ),
                                slice=Name(id='name', ctx=Load()),
                                ctx=Load(),
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
        FunctionDef(
            name='initialize_sys_path',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='\n    Setup the addons path ``odoo.addons.__path__`` with various defaults\n    and explicit directories.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='dd', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='normcase',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                attr='addons_data_dir',
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
                            Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='access',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dd', ctx=Load()),
                                    Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='R_OK',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            Compare(
                                left=Name(id='dd', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='addons',
                                            ctx=Load(),
                                        ),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='addons',
                                            ctx=Load(),
                                        ),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dd', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                For(
                    target=Name(id='ad', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='config',
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
                    body=[
                        Assign(
                            targets=[Name(id='ad', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='normcase',
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
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='ustr',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='ad', ctx=Load()),
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
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='ad', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='addons',
                                            ctx=Load(),
                                        ),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='addons',
                                                    ctx=Load(),
                                                ),
                                                attr='__path__',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ad', ctx=Load())],
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
                Assign(
                    targets=[Name(id='base_path', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='normcase',
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
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='addons', kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                        op=And(),
                        values=[
                            Compare(
                                left=Name(id='base_path', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='addons',
                                            ctx=Load(),
                                        ),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
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
                                args=[Name(id='base_path', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='addons',
                                            ctx=Load(),
                                        ),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='base_path', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                ImportFrom(
                    module='odoo',
                    names=[alias(name='upgrade', asname=None)],
                    level=0,
                ),
                Assign(
                    targets=[Name(id='legacy_upgrade_path', ctx=Store())],
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
                            Name(id='base_path', ctx=Load()),
                            Constant(value='base', kind=None),
                            Constant(value='maintenance', kind=None),
                            Constant(value='migrations', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='up', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='config',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='upgrade_path', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='legacy_upgrade_path', ctx=Load()),
                                ],
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value=',', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='up', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='normcase',
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
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='ustr',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='up', ctx=Load()),
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
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='up', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='upgrade', ctx=Load()),
                                        attr='__path__',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='upgrade', ctx=Load()),
                                                attr='__path__',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='up', ctx=Load())],
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
                Assign(
                    targets=[Name(id='spec', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='importlib', ctx=Load()),
                                attr='machinery',
                                ctx=Load(),
                            ),
                            attr='ModuleSpec',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='odoo.addons.base.maintenance', kind=None),
                            Constant(value=None, kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='is_package',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='maintenance_pkg', ctx=Store())],
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
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='maintenance_pkg', ctx=Load()),
                            attr='migrations',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='upgrade', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Subscript(
                            value=Attribute(
                                value=Name(id='sys', ctx=Load()),
                                attr='modules',
                                ctx=Load(),
                            ),
                            slice=Constant(value='odoo.addons.base.maintenance', kind=None),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='maintenance_pkg', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Subscript(
                            value=Attribute(
                                value=Name(id='sys', ctx=Load()),
                                attr='modules',
                                ctx=Load(),
                            ),
                            slice=Constant(value='odoo.addons.base.maintenance.migrations', kind=None),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='upgrade', ctx=Load()),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='getattr', ctx=Load()),
                            args=[
                                Name(id='initialize_sys_path', ctx=Load()),
                                Constant(value='called', kind=None),
                                Constant(value=False, kind=None),
                            ],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='meta_path',
                                        ctx=Load(),
                                    ),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='UpgradeHook', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='meta_path',
                                        ctx=Load(),
                                    ),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='OdooHook', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='meta_path',
                                        ctx=Load(),
                                    ),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='AddonsHook', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='initialize_sys_path', ctx=Load()),
                                    attr='called',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
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
            name='get_module_path',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='module', annotation=None, type_comment=None),
                    arg(arg='downloaded', annotation=None, type_comment=None),
                    arg(arg='display_warning', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=True, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return the path of the given module.\n\n    Search the addons paths and return the first path where the given\n    module is found. If downloaded is True, return the default addons\n    path if nothing else is found.\n\n    ', kind=None),
                ),
                For(
                    target=Name(id='adp', ctx=Store()),
                    iter=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='addons',
                            ctx=Load(),
                        ),
                        attr='__path__',
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='files', ctx=Store())],
                            value=BinOp(
                                left=ListComp(
                                    elt=Call(
                                        func=Name(id='opj', ctx=Load()),
                                        args=[
                                            Name(id='adp', ctx=Load()),
                                            Name(id='module', ctx=Load()),
                                            Name(id='manifest', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='manifest', ctx=Store()),
                                            iter=Name(id='MANIFEST_NAMES', ctx=Load()),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Call(
                                            func=Name(id='opj', ctx=Load()),
                                            args=[
                                                Name(id='adp', ctx=Load()),
                                                BinOp(
                                                    left=Name(id='module', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value='.zip', kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='f', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='f', ctx=Store()),
                                                iter=Name(id='files', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='opj', ctx=Load()),
                                        args=[
                                            Name(id='adp', ctx=Load()),
                                            Name(id='module', ctx=Load()),
                                        ],
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
                If(
                    test=Name(id='downloaded', ctx=Load()),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='opj', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='config',
                                            ctx=Load(),
                                        ),
                                        attr='addons_data_dir',
                                        ctx=Load(),
                                    ),
                                    Name(id='module', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Name(id='display_warning', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='module %s: module not found', kind=None),
                                    Name(id='module', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
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
            name='get_module_filetree',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='module', annotation=None, type_comment=None),
                    arg(arg='dir', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='.', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=Call(
                        func=Name(id='get_module_path', ctx=Load()),
                        args=[Name(id='module', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='path', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='dir', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='normpath',
                            ctx=Load(),
                        ),
                        args=[Name(id='dir', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='dir', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='.', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='dir', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Call(
                                func=Attribute(
                                    value=Name(id='dir', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='..', kind=None)],
                                keywords=[],
                            ),
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='dir', ctx=Load()),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='dir', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='/', kind=None)],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[Constant(value='Cannot access file outside the module', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='files', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='osutil',
                                ctx=Load(),
                            ),
                            attr='listdir',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='path', ctx=Load()),
                            Constant(value=True, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tree', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                For(
                    target=Name(id='f', ctx=Store()),
                    iter=Name(id='files', ctx=Load()),
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
                                    args=[Name(id='dir', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='dir', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='f', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='f', ctx=Load()),
                                        slice=Slice(
                                            lower=BinOp(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='dir', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Call(
                                                                func=Attribute(
                                                                    value=Name(id='dir', ctx=Load()),
                                                                    attr='endswith',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='/', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lst', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='sep',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current', ctx=Store())],
                            value=Name(id='tree', ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='lst', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='current', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='lst', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='current', ctx=Load()),
                                    slice=Call(
                                        func=Attribute(
                                            value=Name(id='lst', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='tree', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_resource_path',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='module', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return the full path of a resource of the given module.\n\n    :param module: module name\n    :param list(str) args: resource path components within module\n\n    :rtype: str\n    :return: absolute path to the resource\n\n    TODO make it available inside on osv object (self.get_resource_path)\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='mod_path', ctx=Store())],
                    value=Call(
                        func=Name(id='get_module_path', ctx=Load()),
                        args=[Name(id='module', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='mod_path', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='check_resource_path', ctx=Load()),
                        args=[
                            Name(id='mod_path', ctx=Load()),
                            Starred(
                                value=Name(id='args', ctx=Load()),
                                ctx=Load(),
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
            name='check_resource_path',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='mod_path', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='resource_path', ctx=Store())],
                    value=Call(
                        func=Name(id='opj', ctx=Load()),
                        args=[
                            Name(id='mod_path', ctx=Load()),
                            Starred(
                                value=Name(id='args', ctx=Load()),
                                ctx=Load(),
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
                        args=[Name(id='resource_path', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Name(id='resource_path', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=False, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='get_module_resource', ctx=Store())],
            value=Name(id='get_resource_path', ctx=Load()),
            type_comment=None,
        ),
        FunctionDef(
            name='get_resource_from_path',
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
                Expr(
                    value=Constant(value="Tries to extract the module name and the resource's relative path\n    out of an absolute resource path.\n\n    If operation is successful, returns a tuple containing the module name, the relative path\n    to the resource using '/' as filesystem seperator[1] and the same relative path using\n    os.path.sep seperators.\n\n    [1] same convention as the resource path declaration in manifests\n\n    :param path: absolute resource path\n\n    :rtype: tuple\n    :return: tuple(module_name, relative_path, os_relative_path) if possible, else None\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='resource', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='adpath', ctx=Store()),
                    iter=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='addons',
                            ctx=Load(),
                        ),
                        attr='__path__',
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='adpath', ctx=Store())],
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
                                    Name(id='adpath', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='commonprefix',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Name(id='adpath', ctx=Load()),
                                                Name(id='path', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Name(id='adpath', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resource', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='adpath', ctx=Load()),
                                            Constant(value='', kind=None),
                                            Constant(value=1, kind=None),
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
                If(
                    test=Name(id='resource', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='relative', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resource', ctx=Load()),
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
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Name(id='relative', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='relative', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='module', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='relative', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='module', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='/', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='relative', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='sep',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='relative', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
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
            name='get_module_icon',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='module', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='iconpath', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='static', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='icon.png', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Name(id='get_module_resource', ctx=Load()),
                        args=[
                            Name(id='module', ctx=Load()),
                            Starred(
                                value=Name(id='iconpath', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=Constant(value='/', kind=None),
                                        op=Add(),
                                        right=Name(id='module', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Constant(value='/', kind=None),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value='/', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='iconpath', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='/base/', kind=None),
                        op=Add(),
                        right=Call(
                            func=Attribute(
                                value=Constant(value='/', kind=None),
                                attr='join',
                                ctx=Load(),
                            ),
                            args=[Name(id='iconpath', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='module_manifest',
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
                Expr(
                    value=Constant(value='Returns path to module manifest if one can be found under `path`, else `None`.', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='path', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                For(
                    target=Name(id='manifest_name', ctx=Store()),
                    iter=Name(id='MANIFEST_NAMES', ctx=Load()),
                    body=[
                        If(
                            test=Call(
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
                                        func=Name(id='opj', ctx=Load()),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='manifest_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='opj', ctx=Load()),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='manifest_name', ctx=Load()),
                                        ],
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
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='read_manifest',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='addons_path', annotation=None, type_comment=None),
                    arg(arg='module', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='mod_path', ctx=Store())],
                    value=Call(
                        func=Name(id='opj', ctx=Load()),
                        args=[
                            Name(id='addons_path', ctx=Load()),
                            Name(id='module', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='manifest_path', ctx=Store())],
                    value=Call(
                        func=Name(id='module_manifest', ctx=Load()),
                        args=[Name(id='mod_path', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='manifest_path', ctx=Load()),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='file_open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='manifest_path', ctx=Load()),
                                            Constant(value='r', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='fd', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='manifest_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fd', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ast', ctx=Load()),
                                    attr='literal_eval',
                                    ctx=Load(),
                                ),
                                args=[Name(id='manifest_data', ctx=Load())],
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
        FunctionDef(
            name='get_module_root',
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
                Expr(
                    value=Constant(value="\n    Get closest module's root beginning from path\n\n        # Given:\n        # /foo/bar/module_dir/static/src/...\n\n        get_module_root('/foo/bar/module_dir/static/')\n        # returns '/foo/bar/module_dir'\n\n        get_module_root('/foo/bar/module_dir/')\n        # returns '/foo/bar/module_dir'\n\n        get_module_root('/foo/bar')\n        # returns None\n\n    @param path: Path from which the lookup should start\n\n    @return:  Module root path or None if not found\n    ", kind=None),
                ),
                While(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='module_manifest', ctx=Load()),
                            args=[Name(id='path', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_path', ctx=Store())],
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
                                        func=Name(id='opj', ctx=Load()),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='pardir',
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
                        If(
                            test=Compare(
                                left=Name(id='path', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='new_path', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Name(id='new_path', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='path', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='load_information_from_description_file',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='module', annotation=None, type_comment=None),
                    arg(arg='mod_path', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    :param module: The name of the module (sale, purchase, ...)\n    :param mod_path: Physical path of module, if not providedThe name of the module (sale, purchase, ...)\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='mod_path', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mod_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_path', ctx=Load()),
                                args=[Name(id='module', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='downloaded',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='manifest_file', ctx=Store())],
                    value=Call(
                        func=Name(id='module_manifest', ctx=Load()),
                        args=[Name(id='mod_path', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='manifest_file', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='info', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='application', kind=None),
                                    Constant(value='author', kind=None),
                                    Constant(value='auto_install', kind=None),
                                    Constant(value='category', kind=None),
                                    Constant(value='depends', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='icon', kind=None),
                                    Constant(value='installable', kind=None),
                                    Constant(value='post_load', kind=None),
                                    Constant(value='version', kind=None),
                                    Constant(value='web', kind=None),
                                    Constant(value='sequence', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='website', kind=None),
                                ],
                                values=[
                                    Constant(value=False, kind=None),
                                    Constant(value='Odoo S.A.', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value='Uncategorized', kind=None),
                                    List(elts=[], ctx=Load()),
                                    Constant(value='', kind=None),
                                    Call(
                                        func=Name(id='get_module_icon', ctx=Load()),
                                        args=[Name(id='module', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=True, kind=None),
                                    Constant(value=None, kind=None),
                                    Constant(value='1.0', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=100, kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='info', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='depends data demo test init_xml update_xml demo_xml', kind=None),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='iter', ctx=Load()),
                                                args=[
                                                    Name(id='list', ctx=Load()),
                                                    Constant(value=None, kind=None),
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
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='file_open',
                                    ctx=Load(),
                                ),
                                args=[Name(id='manifest_file', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='rb', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='info', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ast', ctx=Load()),
                                                    attr='literal_eval',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='pycompat', ctx=Load()),
                                                            attr='to_text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='f', ctx=Load()),
                                                                    attr='read',
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
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='close',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='info', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='description', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='readme_path', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Name(id='opj', ctx=Load()),
                                            args=[
                                                Name(id='mod_path', ctx=Load()),
                                                Name(id='x', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='README', ctx=Load()),
                                                ifs=[
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
                                                        args=[
                                                            Call(
                                                                func=Name(id='opj', ctx=Load()),
                                                                args=[
                                                                    Name(id='mod_path', ctx=Load()),
                                                                    Name(id='x', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='readme_path', ctx=Load()),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='file_open',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='readme_path', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='fd', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='info', ctx=Load()),
                                                            slice=Constant(value='description', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='fd', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='info', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='license', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='license', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='LGPL-3', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="Missing `license` key in manifest for '%s', defaulting to LGPL-3", kind=None),
                                            Name(id='module', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='info', ctx=Load()),
                                        slice=Constant(value='auto_install', kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='collections', ctx=Load()),
                                            attr='abc',
                                            ctx=Load(),
                                        ),
                                        attr='Iterable',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='auto_install', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='auto_install', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='non_dependencies', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='auto_install', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='difference',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='depends', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='non_dependencies', ctx=Load()),
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='auto_install triggers must be dependencies, found non-dependencies [%s] for module %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Constant(value=', ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='non_dependencies', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Name(id='module', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Subscript(
                                        value=Name(id='info', ctx=Load()),
                                        slice=Constant(value='auto_install', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='info', ctx=Load()),
                                                    slice=Constant(value='auto_install', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='info', ctx=Load()),
                                                        slice=Constant(value='depends', kind=None),
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='info', ctx=Load()),
                                    slice=Constant(value='version', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='adapt_version', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='info', ctx=Load()),
                                        slice=Constant(value='version', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='info', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='module %s: no manifest file found %s', kind=None),
                            Name(id='module', ctx=Load()),
                            Name(id='MANIFEST_NAMES', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Dict(keys=[], values=[]),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='load_openerp_module',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='module_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Load an OpenERP module, if not already loaded.\n\n    This loads the module and register all of its models, thanks to either\n    the MetaModel metaclass, or the explicit instantiation of the model.\n    This is also used to load server-wide module (i.e. it is also used\n    when there is no model to register).\n    ', kind=None),
                ),
                Global(names=['loaded']),
                If(
                    test=Compare(
                        left=Name(id='module_name', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='loaded', ctx=Load())],
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='__import__', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='odoo.addons.', kind=None),
                                        op=Add(),
                                        right=Name(id='module_name', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='info', ctx=Store())],
                            value=Call(
                                func=Name(id='load_information_from_description_file', ctx=Load()),
                                args=[Name(id='module_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='info', ctx=Load()),
                                slice=Constant(value='post_load', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='sys', ctx=Load()),
                                                        attr='modules',
                                                        ctx=Load(),
                                                    ),
                                                    slice=BinOp(
                                                        left=Constant(value='odoo.addons.', kind=None),
                                                        op=Add(),
                                                        right=Name(id='module_name', ctx=Load()),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='info', ctx=Load()),
                                                    slice=Constant(value='post_load', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value="Couldn't load module %s", kind=None),
                                        op=Mod(),
                                        right=Name(id='module_name', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='critical',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='msg', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='critical',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='e', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Raise(exc=None, cause=None),
                            ],
                        ),
                    ],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='loaded', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='module_name', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_modules',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='Returns the list of module names\n    ', kind=None),
                ),
                FunctionDef(
                    name='listdir',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='dir', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='clean',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='name', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='basename',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='name', ctx=Load()),
                                            slice=Slice(
                                                lower=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=4, kind=None),
                                                ),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='.zip', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='name', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=4, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='name', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='is_really_module',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='name', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='mname', ctx=Store()),
                                    iter=Name(id='MANIFEST_NAMES', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
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
                                                        func=Name(id='opj', ctx=Load()),
                                                        args=[
                                                            Name(id='dir', ctx=Load()),
                                                            Name(id='name', ctx=Load()),
                                                            Name(id='mname', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='clean', ctx=Load()),
                                    args=[Name(id='it', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='it', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='listdir',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='dir', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Call(
                                                func=Name(id='is_really_module', ctx=Load()),
                                                args=[Name(id='it', ctx=Load())],
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
                Assign(
                    targets=[Name(id='plist', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='ad', ctx=Store()),
                    iter=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='addons',
                            ctx=Load(),
                        ),
                        attr='__path__',
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='plist', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='listdir', ctx=Load()),
                                        args=[Name(id='ad', ctx=Load())],
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
                Return(
                    value=Call(
                        func=Name(id='list', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='set', ctx=Load()),
                                args=[Name(id='plist', ctx=Load())],
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
            name='get_modules_with_version',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='modules', ctx=Store())],
                    value=Call(
                        func=Name(id='get_modules', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='dict', ctx=Load()),
                            attr='fromkeys',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='modules', ctx=Load()),
                            Call(
                                func=Name(id='adapt_version', ctx=Load()),
                                args=[Constant(value='1.0', kind=None)],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='module', ctx=Store()),
                    iter=Name(id='modules', ctx=Load()),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='info', ctx=Store())],
                                    value=Call(
                                        func=Name(id='load_information_from_description_file', ctx=Load()),
                                        args=[Name(id='module', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='module', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='info', ctx=Load()),
                                        slice=Constant(value='version', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[Continue()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='adapt_version',
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
                Assign(
                    targets=[Name(id='serie', ctx=Store())],
                    value=Attribute(
                        value=Name(id='release', ctx=Load()),
                        attr='major_version',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Name(id='version', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='serie', ctx=Load())],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='version', ctx=Load()),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        BinOp(
                                            left=Name(id='serie', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value='.', kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='version', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s.%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='serie', ctx=Load()),
                                        Name(id='version', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='version', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='current_test', ctx=Store())],
            value=Constant(value=None, kind=None),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
