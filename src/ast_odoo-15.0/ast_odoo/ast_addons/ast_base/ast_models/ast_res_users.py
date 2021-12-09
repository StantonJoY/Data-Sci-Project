Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='binascii', asname=None)],
        ),
        Import(
            names=[alias(name='contextlib', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='hmac', asname=None)],
        ),
        Import(
            names=[alias(name='ipaddress', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='hashlib',
            names=[alias(name='sha256', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='itertools',
            names=[
                alias(name='chain', asname=None),
                alias(name='repeat', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='decorator', asname=None)],
        ),
        Import(
            names=[alias(name='passlib.context', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml.builder',
            names=[alias(name='E', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_model',
            names=[alias(name='MODULE_UNINSTALL_FLAG', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='AccessDenied', asname=None),
                alias(name='AccessError', asname=None),
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_module_resource', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.service.db',
            names=[alias(name='check_super', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='partition', asname=None),
                alias(name='collections', asname=None),
                alias(name='frozendict', asname=None),
                alias(name='lazy_property', asname=None),
                alias(name='image_process', asname=None),
            ],
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
        Assign(
            targets=[Name(id='USER_PRIVATE_FIELDS', ctx=Store())],
            value=List(elts=[], ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_CRYPT_CONTEXT', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='passlib', ctx=Load()),
                        attr='context',
                        ctx=Load(),
                    ),
                    attr='CryptContext',
                    ctx=Load(),
                ),
                args=[
                    List(
                        elts=[
                            Constant(value='pbkdf2_sha512', kind=None),
                            Constant(value='plaintext', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[
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
        Assign(
            targets=[Name(id='concat', ctx=Store())],
            value=Attribute(
                value=Name(id='chain', ctx=Load()),
                attr='from_iterable',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='name_boolean_group',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='id', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=BinOp(
                        left=Constant(value='in_group_', kind=None),
                        op=Add(),
                        right=Call(
                            func=Name(id='str', ctx=Load()),
                            args=[Name(id='id', ctx=Load())],
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
            name='name_selection_groups',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='ids', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=BinOp(
                        left=Constant(value='sel_groups_', kind=None),
                        op=Add(),
                        right=Call(
                            func=Attribute(
                                value=Constant(value='_', kind=None),
                                attr='join',
                                ctx=Load(),
                            ),
                            args=[
                                GeneratorExp(
                                    elt=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Name(id='it', ctx=Load())],
                                        keywords=[],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='it', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[Name(id='ids', ctx=Load())],
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
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='is_boolean_group',
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
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='name', ctx=Load()),
                            attr='startswith',
                            ctx=Load(),
                        ),
                        args=[Constant(value='in_group_', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='is_selection_groups',
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
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='name', ctx=Load()),
                            attr='startswith',
                            ctx=Load(),
                        ),
                        args=[Constant(value='sel_groups_', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='is_reified_group',
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
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Call(
                                func=Name(id='is_boolean_group', ctx=Load()),
                                args=[Name(id='name', ctx=Load())],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='is_selection_groups', ctx=Load()),
                                args=[Name(id='name', ctx=Load())],
                                keywords=[],
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
            name='get_boolean_group',
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
                Return(
                    value=Call(
                        func=Name(id='int', ctx=Load()),
                        args=[
                            Subscript(
                                value=Name(id='name', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=9, kind=None),
                                    upper=None,
                                    step=None,
                                ),
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
            name='get_selection_groups',
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
                Return(
                    value=ListComp(
                        elt=Call(
                            func=Name(id='int', ctx=Load()),
                            args=[Name(id='v', ctx=Load())],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='v', ctx=Store()),
                                iter=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='name', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=11, kind=None),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='_', kind=None)],
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
        FunctionDef(
            name='parse_m2m',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='commands', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='return a list of ids corresponding to a many2many value', kind=None),
                ),
                Assign(
                    targets=[Name(id='ids', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='command', ctx=Store()),
                    iter=Name(id='commands', ctx=Load()),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='command', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='tuple', ctx=Load()),
                                            Name(id='list', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='command', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='UPDATE',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='LINK',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='command', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='command', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='CLEAR',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ids', ctx=Store())],
                                                    value=List(elts=[], ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='command', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='Command', ctx=Load()),
                                                                attr='SET',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='ids', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='list', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='command', ctx=Load()),
                                                                        slice=Constant(value=2, kind=None),
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
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='command', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='ids', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_jsonable',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='o', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[Name(id='o', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='TypeError', ctx=Load()),
                            name=None,
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    orelse=[
                        Return(
                            value=Constant(value=True, kind=None),
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
            name='check_identity',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='fn', annotation=None, type_comment=None),
                    arg(arg='self', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Wrapped method should be an *action method* (called from a button\n    type=object), and requires extra security to be executed. This decorator\n    checks if the identity (password) has been checked in the last 10mn, and\n    pops up an identity check wizard if not.\n\n    Prevents access outside of interactive contexts (aka with a request)\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='request', ctx=Load()),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='This method can only be accessed over HTTP', kind=None)],
                                        keywords=[],
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
                        left=Call(
                            func=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='get',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='identity-check-last', kind=None),
                                Constant(value=0, kind=None),
                            ],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[
                            BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='time', ctx=Load()),
                                        attr='time',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=BinOp(
                                    left=Constant(value=10, kind=None),
                                    op=Mult(),
                                    right=Constant(value=60, kind=None),
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='fn', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='w', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users.identitycheck', kind=None),
                                ctx=Load(),
                            ),
                            attr='create',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[Constant(value='request', kind=None)],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    DictComp(
                                                        key=Name(id='k', ctx=Load()),
                                                        value=Name(id='v', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='k', ctx=Store()),
                                                                        Name(id='v', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='context',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='items',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[
                                                                    Call(
                                                                        func=Name(id='_jsonable', ctx=Load()),
                                                                        args=[Name(id='v', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='fn', ctx=Load()),
                                                        attr='__name__',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Dict(
                        keys=[
                            Constant(value='type', kind=None),
                            Constant(value='res_model', kind=None),
                            Constant(value='res_id', kind=None),
                            Constant(value='name', kind=None),
                            Constant(value='target', kind=None),
                            Constant(value='views', kind=None),
                        ],
                        values=[
                            Constant(value='ir.actions.act_window', kind=None),
                            Constant(value='res.users.identitycheck', kind=None),
                            Attribute(
                                value=Name(id='w', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Security Control', kind=None)],
                                keywords=[],
                            ),
                            Constant(value='new', kind=None),
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value='form', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[
                Attribute(
                    value=Name(id='decorator', ctx=Load()),
                    attr='decorator',
                    ctx=Load(),
                ),
            ],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Groups',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='res.groups', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Access Groups', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='full_name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='users', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='res_groups_users_rel', kind=None),
                            Constant(value='gid', kind=None),
                            Constant(value='uid', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_access', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.model.access', kind=None),
                            Constant(value='group_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Access Controls', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rule_groups', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.rule', kind=None),
                            Constant(value='rule_group_rel', kind=None),
                            Constant(value='group_id', kind=None),
                            Constant(value='rule_group_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Rules', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='global', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='menu_access', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.ui.menu', kind=None),
                            Constant(value='ir_ui_menu_group_rel', kind=None),
                            Constant(value='gid', kind=None),
                            Constant(value='menu_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Access Menu', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='view_access', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.ui.view', kind=None),
                            Constant(value='ir_ui_view_group_rel', kind=None),
                            Constant(value='group_id', kind=None),
                            Constant(value='view_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Views', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='comment', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='category_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.module.category', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Application', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Color Index', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='full_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_full_name', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Group Name', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_full_name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='share', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Share Group', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Group created to set access rights for sharing data with some users.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='name_uniq', kind=None),
                                    Constant(value='unique (category_id, name)', kind=None),
                                    Constant(value='The name of the group must be unique within an application!', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_one_user_type',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='users',
                                        ctx=Load(),
                                    ),
                                    attr='_check_one_user_type',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='users', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_full_name',
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='group', ctx=Store()),
                                    Name(id='group1', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='group1', ctx=Load()),
                                        attr='category_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='group', ctx=Load()),
                                                    attr='full_name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='%s / %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='group1', ctx=Load()),
                                                                attr='category_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='group1', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='group', ctx=Load()),
                                                    attr='full_name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='group1', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='category_id.name', kind=None),
                                Constant(value='name', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_full_name',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='operand', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lst', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='operand', ctx=Load()),
                                    Name(id='bool', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domains', ctx=Store())],
                                    value=List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='name', kind=None),
                                                            Name(id='operator', ctx=Load()),
                                                            Name(id='operand', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='category_id.name', kind=None),
                                                            Name(id='operator', ctx=Load()),
                                                            Name(id='operand', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='operator', ctx=Load()),
                                        ops=[
                                            In(),
                                            Eq(),
                                        ],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='expression', ctx=Load()),
                                                attr='NEGATIVE_TERM_OPERATORS',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='operand', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domains', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='OR',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domains', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='operand', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lst', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='operand', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='operand', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='where', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Name(id='operand', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='v', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='v', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='group', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='/', kind=None)],
                                                    keywords=[],
                                                ),
                                                ifs=[Name(id='v', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='group_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='category_name', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='values', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Constant(value='/', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='values', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='strip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Name(id='group_name', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='group_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Name(id='operator', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='lst', ctx=Load()),
                                                                    List(
                                                                        elts=[Name(id='group_name', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='group_name', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='category_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='category_id.name', kind=None),
                                                    Name(id='operator', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='lst', ctx=Load()),
                                                                    List(
                                                                        elts=[Name(id='category_name', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='category_name', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='expression', ctx=Load()),
                                                        attr='NEGATIVE_TERM_OPERATORS',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='values', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='category_domain', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='OR',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='category_domain', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='category_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                If(
                                    test=Compare(
                                        left=Compare(
                                            left=Name(id='operator', ctx=Load()),
                                            ops=[In()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='NEGATIVE_TERM_OPERATORS',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='values', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sub_where', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='group_domain', ctx=Load()),
                                                            Name(id='category_domain', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='sub_where', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='OR',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='group_domain', ctx=Load()),
                                                            Name(id='category_domain', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='operator', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='expression', ctx=Load()),
                                                attr='NEGATIVE_TERM_OPERATORS',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='where', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='where', ctx=Load()),
                                                            Name(id='sub_where', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='where', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='OR',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='where', ctx=Load()),
                                                            Name(id='sub_where', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='where', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                            arg(arg='access_rights_uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='order', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='full_name', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='groups', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Groups', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='groups', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='groups', ctx=Load()),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='full_name', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='reverse',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='endswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='DESC', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='groups', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='limit', ctx=Load()),
                                        body=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Slice(
                                                lower=Name(id='offset', ctx=Load()),
                                                upper=BinOp(
                                                    left=Name(id='offset', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='limit', ctx=Load()),
                                                ),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        orelse=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Slice(
                                                lower=Name(id='offset', ctx=Load()),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=IfExp(
                                        test=Name(id='count', ctx=Load()),
                                        body=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='groups', ctx=Load())],
                                            keywords=[],
                                        ),
                                        orelse=Attribute(
                                            value=Name(id='groups', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Groups', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='count',
                                        value=Name(id='count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='access_rights_uid',
                                        value=Name(id='access_rights_uid', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='chosen_name', ctx=Store())],
                            value=IfExp(
                                test=Name(id='default', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='default', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='name', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_name', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='chosen_name', ctx=Load()),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='%s (copy)', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='default', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Name(id='default_name', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Groups', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='name', kind=None),
                                ops=[In()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='-', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The name of the group can not start with "-"', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model.access', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='call_cache_clearing_methods',
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
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.users', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            attr='clear_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Groups', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
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
        ClassDef(
            name='ResUsersLog',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='res.users.log', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='id desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Users Log', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_gc_user_logs',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            DELETE FROM res_users_log log1 WHERE EXISTS (\n                SELECT 1 FROM res_users_log log2\n                WHERE log1.create_uid = log2.create_uid\n                AND log1.create_date < log2.create_date\n            )\n        ', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="GC'd %d user log entries", kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        attr='rowcount',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='autovacuum',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Users',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' User class. A res.users record models an OpenERP user and is different\n        from an employee.\n\n        res.users class now inherits from res.partner. The partner model is\n        used to store the data related to the partner: lang, name, address,\n        avatar, ... The user model is now dedicated to technical data.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Users', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherits', ctx=Store())],
                    value=Dict(
                        keys=[Constant(value='res.partner', kind=None)],
                        values=[Constant(value='partner_id', kind=None)],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name, login', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='SELF_READABLE_FIELDS',
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
                        Expr(
                            value=Constant(value=' The list of fields a user can read on their own user record.\n        In order to add fields, please override this property on model extensions.\n        ', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='signature', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='login', kind=None),
                                    Constant(value='email', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='image_1920', kind=None),
                                    Constant(value='image_1024', kind=None),
                                    Constant(value='image_512', kind=None),
                                    Constant(value='image_256', kind=None),
                                    Constant(value='image_128', kind=None),
                                    Constant(value='lang', kind=None),
                                    Constant(value='tz', kind=None),
                                    Constant(value='tz_offset', kind=None),
                                    Constant(value='groups_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='__last_update', kind=None),
                                    Constant(value='action_id', kind=None),
                                    Constant(value='avatar_1920', kind=None),
                                    Constant(value='avatar_1024', kind=None),
                                    Constant(value='avatar_512', kind=None),
                                    Constant(value='avatar_256', kind=None),
                                    Constant(value='avatar_128', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='SELF_WRITEABLE_FIELDS',
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
                        Expr(
                            value=Constant(value=' The list of fields a user can write on their own user record.\n        In order to add fields, please override this property on model extensions.\n        ', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='signature', kind=None),
                                    Constant(value='action_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='email', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='image_1920', kind=None),
                                    Constant(value='lang', kind=None),
                                    Constant(value='tz', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_groups',
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
                            targets=[Name(id='default_user_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.default_user', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='default_user_id', ctx=Load()),
                                body=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.users', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='default_user_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='groups_id',
                                    ctx=Load(),
                                ),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='auto_join',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Related Partner', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Partner-related data of the user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='login', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Used to log into the system', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='password', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_password', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_password', kind=None),
                            ),
                            keyword(
                                arg='invisible',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Keep empty if you don't want the user to be able to connect on the system.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_password', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Set Password', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_password', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_new_password', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Specify a value only when creating a user or if you're changing the user's password, otherwise leave empty. After a change of password, the user has to login again.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='signature', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Email Signature', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active_partner', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.active', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Partner is Active', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='action_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.actions.actions', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Home Action', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If specified, this action will be opened at log on for this user, in addition to the standard menu.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='groups_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.groups', kind=None),
                            Constant(value='res_groups_users_rel', kind=None),
                            Constant(value='uid', kind=None),
                            Constant(value='gid', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Groups', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_groups', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='log_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users.log', kind=None),
                            Constant(value='create_uid', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='User log entries', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='login_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='log_ids.create_date', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Latest authentication', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='share', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_share', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Share User', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='External user with limited access, created only for the purpose of sharing data.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='companies_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_companies_count', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Companies', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tz_offset', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_tz_offset', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Timezone offset', kind=None),
                            ),
                            keyword(
                                arg='invisible',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The default company for this user.', kind=None),
                            ),
                            keyword(
                                arg='context',
                                value=Dict(
                                    keys=[Constant(value='user_preference', kind=None)],
                                    values=[Constant(value=True, kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='res_company_users_rel', kind=None),
                            Constant(value='user_id', kind=None),
                            Constant(value='cid', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Companies', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.name', kind=None),
                            ),
                            keyword(
                                arg='inherited',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.email', kind=None),
                            ),
                            keyword(
                                arg='inherited',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='accesses_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='# Access Rights', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Number of access rights that apply to the current user', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_accesses_count', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rules_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='# Record Rules', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Number of record rules that apply to the current user', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_accesses_count', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='groups_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='# Groups', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Number of groups that apply to the current user', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_accesses_count', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='login_key', kind=None),
                                    Constant(value='UNIQUE (login)', kind=None),
                                    Constant(value='You can not have two users with the same login !', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                            targets=[Name(id='cr', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='cr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="\n        SELECT id, password FROM res_users\n        WHERE password IS NOT NULL\n          AND password !~ '^\\$[^$]+\\$[^$]+\\$.'\n        ", kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='cr',
                                    ctx=Load(),
                                ),
                                attr='rowcount',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='Users', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='uid', ctx=Store()),
                                            Name(id='pw', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='fetchall',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Users', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='uid', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='password',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='pw', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                    name='_set_password',
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
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_crypt_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hash_password', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='ctx', ctx=Load()),
                                        Constant(value='hash', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                body=Attribute(
                                    value=Name(id='ctx', ctx=Load()),
                                    attr='hash',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Name(id='ctx', ctx=Load()),
                                    attr='encrypt',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_set_encrypted_password',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='hash_password', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='password',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_encrypted_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
                            arg(arg='pw', annotation=None, type_comment=None),
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
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_crypt_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='identify',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='pw', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='plaintext', kind=None)],
                            ),
                            msg=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='UPDATE res_users SET password=%s WHERE id=%s', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='pw', ctx=Load()),
                                            Name(id='uid', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='password', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Name(id='uid', ctx=Load())],
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
                    name='_check_credentials',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Validates the current user's password.\n\n        Override this method to plug additional authentication methods.\n\n        Overrides should:\n\n        * call `super` to delegate to parents for credentials-checking\n        * catch AccessDenied and perform their own checking\n        * (re)raise AccessDenied if the credentials are still invalid\n          according to their own validation method\n\n        When trying to check for credentials validity, call _check_credentials\n        instead.\n        ", kind=None),
                        ),
                        Expr(
                            value=Constant(value=' Override this method to plug additional authentication methods', kind=None),
                        ),
                        Assert(
                            test=Name(id='password', ctx=Load()),
                            msg=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="SELECT COALESCE(password, '') FROM res_users WHERE id=%s", kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='hashed', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='valid', ctx=Store()),
                                        Name(id='replacement', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_crypt_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='verify_and_update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='password', ctx=Load()),
                                    Name(id='hashed', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='replacement', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_set_encrypted_password',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='replacement', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='valid', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessDenied', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
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
                    name='_compute_password',
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
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='password',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='new_password',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='', kind=None),
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
                    name='_set_new_password',
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
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='new_password',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='user', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Please use the change password wizard (in User Preferences or User menu) to change your own password.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='password',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='new_password',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
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
                    name='_compute_share',
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
                            targets=[Name(id='user_group_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_user', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='internal_users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='groups_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[Name(id='user_group_id', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                    value=Name(id='internal_users', ctx=Load()),
                                    attr='share',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=BinOp(
                                        left=Name(id='self', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='internal_users', ctx=Load()),
                                    ),
                                    attr='share',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='groups_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_companies_count',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='companies_count',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
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
                    name='_compute_tz_offset',
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
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='tz_offset',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='pytz', ctx=Load()),
                                                            attr='timezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='user', ctx=Load()),
                                                                        attr='tz',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='GMT', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%z', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='tz', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_accesses_count',
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
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='groups', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='groups_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='accesses_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='groups', ctx=Load()),
                                                attr='model_access',
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
                                            value=Name(id='user', ctx=Load()),
                                            attr='rules_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='groups', ctx=Load()),
                                                attr='rule_groups',
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
                                            value=Name(id='user', ctx=Load()),
                                            attr='groups_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='groups', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='groups_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='on_change_login',
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='login',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='single_email_re',
                                                ctx=Load(),
                                            ),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='login',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='email',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='login',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='login', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange_parent_id',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='onchange_parent_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='parent_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_read',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='canwrite', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_exception',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='canwrite', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[Name(id='USER_PRIVATE_FIELDS', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='intersection',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fields', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='f', ctx=Store()),
                                            iter=Name(id='USER_PRIVATE_FIELDS', ctx=Load()),
                                            body=[
                                                Try(
                                                    body=[
                                                        Expr(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='_cache',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='f', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='_cache',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='f', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='********', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='Exception', ctx=Load()),
                                                            name=None,
                                                            body=[Pass()],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
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
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_company',
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
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='company_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Company %(company_name)s is not in the allowed companies for user %(user_name)s (%(company_allowed)s).', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='company_name',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='user', ctx=Load()),
                                                                        attr='company_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='user_name',
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='company_allowed',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Constant(value=', ', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='user', ctx=Load()),
                                                                                attr='mapped',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='company_ids.name', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='company_id', kind=None),
                                Constant(value='company_ids', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_action_id',
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
                            targets=[Name(id='action_open_website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.action_open_website', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='action_open_website', ctx=Load()),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='action_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='action_open_website', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='user', ctx=Store()),
                                                        iter=Name(id='self', ctx=Load()),
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
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The "App Switcher" action cannot be selected as home action.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='action_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_one_user_type',
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
                        Expr(
                            value=Constant(value='We check that no users are both portal and users (same with public).\n           This could typically happen because of implied groups.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='user_types_category', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.module_category_user_type', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_types_groups', ctx=Store())],
                            value=IfExp(
                                test=Name(id='user_types_category', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.groups', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='category_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Name(id='user_types_category', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='user_types_groups', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_has_multiple_groups',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='user_types_groups', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The user cannot have more than one user types.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='groups_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_has_multiple_groups',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='The method is not fast if the list of ids is very long;\n           so we rather check all users than limit to the size of the group\n        :param group_ids: list of group ids\n        :return: boolean: is there at least a user in at least 2 of the provided groups\n        ', kind=None),
                        ),
                        If(
                            test=Name(id='group_ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='group_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='where_clause', ctx=Store())],
                                            value=Constant(value='AND r.uid = %s', kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='where_clause', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Constant(value='\n                    SELECT 1 FROM res_groups_users_rel WHERE EXISTS(\n                        SELECT r.uid\n                        FROM res_groups_users_rel r\n                        WHERE r.gid IN %s', kind=None),
                                            op=Add(),
                                            right=Name(id='where_clause', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Constant(value='\n                        GROUP BY r.uid HAVING COUNT(r.gid) > 1\n                    )\n            ', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='query', ctx=Load()),
                                            Name(id='args', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='fetchall',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='toggle_active',
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
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='active',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='active',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='toggle_active',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='toggle_active',
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
                    name='read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='load', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='_classic_read', kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='fields', ctx=Load()),
                                    Compare(
                                        left=Name(id='self', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='readable', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SELF_READABLE_FIELDS',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='key', ctx=Store()),
                                    iter=Name(id='fields', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Compare(
                                                            left=Name(id='key', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[Name(id='readable', ctx=Load())],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='key', ctx=Load()),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='context_', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=Name(id='fields', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='load',
                                        value=Name(id='load', ctx=Load()),
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
                    name='read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='groupby_fields', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    IfExp(
                                        test=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='groupby', ctx=Load()),
                                                Name(id='str', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        body=List(
                                            elts=[Name(id='groupby', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                        orelse=Name(id='groupby', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='groupby_fields', ctx=Load()),
                                    attr='intersection',
                                    ctx=Load(),
                                ),
                                args=[Name(id='USER_PRIVATE_FIELDS', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Invalid 'group by' parameter", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Name(id='orderby', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lazy',
                                        value=Name(id='lazy', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                            arg(arg='access_rights_uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='su',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Name(id='args', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain_fields', ctx=Store())],
                                    value=SetComp(
                                        elt=Subscript(
                                            value=Name(id='term', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='term', ctx=Store()),
                                                iter=Name(id='args', ctx=Load()),
                                                ifs=[
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='term', ctx=Load()),
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='tuple', ctx=Load()),
                                                                    Name(id='list', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
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
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='domain_fields', ctx=Load()),
                                            attr='intersection',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='USER_PRIVATE_FIELDS', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AccessError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Invalid search criterion', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='count',
                                        value=Name(id='count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='access_rights_uid',
                                        value=Name(id='access_rights_uid', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='users', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='active',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='users', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='active', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Name(id='SUPERUSER_ID', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You cannot activate the superuser.', kind=None)],
                                                keywords=[],
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='active', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=False, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_uid',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="You cannot deactivate the user you're currently logged in as.", kind=None)],
                                                keywords=[],
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='active', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='user', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='active',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='active',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='toggle_active',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='self', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='writeable', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SELF_WRITEABLE_FIELDS',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='key', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Compare(
                                                            left=Name(id='key', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[Name(id='writeable', ctx=Load())],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='key', ctx=Load()),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='context_', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='company_id', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='values', ctx=Load())],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='company_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='user',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='company_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Delete(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='company_id', kind=None),
                                                                    ctx=Del(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='binary_field_real_user',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='company_id', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                For(
                                    target=Name(id='user', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='company_id', kind=None),
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
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='company_id', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
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
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='company_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='company_ids', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='env', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='transaction',
                                                    ctx=Load(),
                                                ),
                                                attr='envs',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='env', ctx=Load()),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='self', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lazy_property', ctx=Load()),
                                                            attr='reset_all',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='env', ctx=Load())],
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
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Constant(value='groups_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model.access', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='call_cache_clearing_methods',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='invalidation_fields', ctx=Store())],
                            value=Set(
                                elts=[
                                    Constant(value='groups_id', kind=None),
                                    Constant(value='active', kind=None),
                                    Constant(value='lang', kind=None),
                                    Constant(value='tz', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Starred(
                                        value=Name(id='USER_PRIVATE_FIELDS', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Starred(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_session_token_fields',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BinOp(
                                        left=Name(id='invalidation_fields', ctx=Load()),
                                        op=BitAnd(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='keys',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='key', ctx=Load()),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='context_', kind=None)],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='key', ctx=Store()),
                                                        iter=Name(id='values', ctx=Load()),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clear_caches',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                    name='_unlink_except_superuser',
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
                            test=Compare(
                                left=Name(id='SUPERUSER_ID', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You can not remove the admin user as it is used internally for resources created by Odoo (updates, module installation, ...)', kind=None)],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='ondelete',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='at_uninstall',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_name_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='name_get_uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='ilike', kind=None),
                            Constant(value=100, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='args', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='expression', ctx=Load()),
                                        attr='NEGATIVE_TERM_OPERATORS',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='ilike', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Name(id='name', ctx=Load()),
                                                                Constant(value='', kind=None),
                                                            ],
                                                        ),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='login', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='name', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='user_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='domain', ctx=Load()),
                                                            Name(id='args', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='access_rights_uid',
                                                value=Name(id='name_get_uid', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='user_ids', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='user_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='name', kind=None),
                                                                            Name(id='operator', ctx=Load()),
                                                                            Name(id='name', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='args', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='access_rights_uid',
                                                value=Name(id='name_get_uid', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='user_ids', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='default', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
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
                                        left=Constant(value='name', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='default', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='partner_id', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='default', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='default', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='%s (copy)', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='name',
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
                        If(
                            test=Compare(
                                left=Constant(value='login', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='default', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='default', ctx=Load()),
                                            slice=Constant(value='login', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='%s (copy)', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='login',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='context_get',
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
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name_to_key', ctx=Store())],
                            value=DictComp(
                                key=Name(id='name', ctx=Load()),
                                value=IfExp(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='name', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='context_', kind=None)],
                                        keywords=[],
                                    ),
                                    body=Subscript(
                                        value=Name(id='name', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=8, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    orelse=Name(id='name', ctx=Load()),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='name', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        ifs=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='name', ctx=Load()),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='context_', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Name(id='name', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='lang', kind=None),
                                                                    Constant(value='tz', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='read',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='list', ctx=Load()),
                                            args=[Name(id='name_to_key', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='load',
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='frozendict', ctx=Load()),
                                args=[
                                    DictComp(
                                        key=Name(id='key', ctx=Load()),
                                        value=Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Name(id='name', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='name', ctx=Store()),
                                                        Name(id='key', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='name_to_key', ctx=Load()),
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
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[Constant(value='self._uid', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_get',
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
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.action_res_users_my', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='read',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_super',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='passwd', annotation=None, type_comment=None),
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
                                func=Name(id='check_super', ctx=Load()),
                                args=[Name(id='passwd', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_last_login',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users.log', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_login_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='login', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='login', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_login_order',
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
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_order',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_login',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='user_agent_env', annotation=None, type_comment=None),
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
                                operand=Name(id='password', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessDenied', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='ip', ctx=Store())],
                            value=IfExp(
                                test=Name(id='request', ctx=Load()),
                                body=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='REMOTE_ADDR', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Constant(value='n/a', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='pool',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='cr', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='api', ctx=Load()),
                                                        attr='Environment',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='cr', ctx=Load()),
                                                        Name(id='SUPERUSER_ID', ctx=Load()),
                                                        Dict(keys=[], values=[]),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_assert_can_auth',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='user', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_get_login_domain',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='login', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='order',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_get_login_order',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='limit',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='user', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='AccessDenied', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='user', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='user', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='_check_credentials',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='password', ctx=Load()),
                                                            Name(id='user_agent_env', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='tz', ctx=Store())],
                                                    value=IfExp(
                                                        test=Name(id='request', ctx=Load()),
                                                        body=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='httprequest',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='cookies',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='tz', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        orelse=Constant(value=None, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='tz', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='pytz', ctx=Load()),
                                                                        attr='all_timezones',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='tz',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='login_date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='tz',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='tz', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='_update_last_login',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessDenied', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Login failed for db:%s login:%s from %s', kind=None),
                                                    Name(id='db', ctx=Load()),
                                                    Name(id='login', ctx=Load()),
                                                    Name(id='ip', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(exc=None, cause=None),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Login successful for db:%s login:%s from %s', kind=None),
                                    Name(id='db', ctx=Load()),
                                    Name(id='login', ctx=Load()),
                                    Name(id='ip', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='user', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='authenticate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='user_agent_env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Verifies and returns the user ID corresponding to the given\n          ``login`` and ``password`` combination, or False if there was\n          no matching user.\n           :param str db: the database on which user is trying to authenticate\n           :param str login: username\n           :param str password: user password\n           :param dict user_agent_env: environment dictionary describing any\n               relevant environment attributes\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_login',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='db', ctx=Load()),
                                    Name(id='login', ctx=Load()),
                                    Name(id='password', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user_agent_env',
                                        value=Name(id='user_agent_env', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='user_agent_env', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='user_agent_env', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base_location', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='pool',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='cr', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='api', ctx=Load()),
                                                    attr='Environment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='uid', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='env', ctx=Load()),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='has_group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='base.group_system', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='base', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='user_agent_env', ctx=Load()),
                                                                slice=Constant(value='base_location', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='ICP', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='ICP', ctx=Load()),
                                                                        attr='get_param',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='web.base.url.freeze', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='ICP', ctx=Load()),
                                                                            attr='set_param',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='web.base.url', kind=None),
                                                                            Name(id='base', ctx=Load()),
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
                                                            type=Name(id='Exception', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='exception',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='Failed to update web.base.url configuration parameter', kind=None)],
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
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='uid', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
                            arg(arg='passwd', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Verifies that the given (uid, password) is authorized for the database ``db`` and\n           raise an exception if it is not.', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='passwd', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessDenied', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='contextlib', ctx=Load()),
                                            attr='closing',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='pool',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='self', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='api', ctx=Load()),
                                                attr='Environment',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='cr', ctx=Load()),
                                                Name(id='uid', ctx=Load()),
                                                Dict(keys=[], values=[]),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_assert_can_auth',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='active',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='AccessDenied', ctx=Load()),
                                                        args=[],
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
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_check_credentials',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='passwd', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='interactive', kind=None)],
                                                        values=[Constant(value=False, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Name(id='classmethod', ctx=Load()),
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='uid', kind=None),
                                Constant(value='passwd', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_session_token_fields',
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
                        Return(
                            value=Set(
                                elts=[
                                    Constant(value='id', kind=None),
                                    Constant(value='login', kind=None),
                                    Constant(value='password', kind=None),
                                    Constant(value='active', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_session_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compute a session token given a session id and a user id ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='session_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=', ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_session_token_fields',
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value="SELECT %s, (SELECT value FROM ir_config_parameter WHERE key='database.secret')\n                                FROM res_users\n                                WHERE id=%%s", kind=None),
                                        op=Mod(),
                                        right=Name(id='session_fields', ctx=Load()),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='rowcount',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clear_caches',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='data_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Constant(value='%s', kind='u'),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='data_fields', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sid', ctx=Load()),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='h', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='hmac', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='key', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                    Name(id='sha256', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='h', ctx=Load()),
                                    attr='hexdigest',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[Constant(value='sid', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='change_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='old_passwd', annotation=None, type_comment=None),
                            arg(arg='new_passwd', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Change current user password. Old password must be provided explicitly\n        to prevent hijacking an existing user session, or for cases where the cleartext\n        password is not used to authenticate requests.\n\n        :return: True\n        :raise: odoo.exceptions.AccessDenied when old password is wrong\n        :raise: odoo.exceptions.UserError when new password is not set or empty\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='old_passwd', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessDenied', ctx=Load()),
                                        args=[],
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
                                operand=Name(id='new_passwd', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Setting empty passwords is not allowed for security reasons!', kind=None)],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_credentials',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='old_passwd', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='interactive', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ip', ctx=Store())],
                            value=IfExp(
                                test=Name(id='request', ctx=Load()),
                                body=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='REMOTE_ADDR', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Constant(value='n/a', kind=None),
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
                                    Constant(value="Password change for '%s' (#%s) from %s", kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='login',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Name(id='ip', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='password', kind=None)],
                                        values=[Name(id='new_passwd', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='preference_save',
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='tag', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.client', kind=None),
                                    Constant(value='reload_context', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='preference_change_password',
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.client', kind=None),
                                    Constant(value='change_password', kind=None),
                                    Constant(value='new', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='has_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_ext_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_uid',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='uid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_has_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='group_ext_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_has_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_ext_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Checks whether user belongs to given group.\n\n        :param str group_ext_id: external ID (XML ID) of the group.\n           Must be provided in fully-qualified form (``module.ext_id``), as there\n           is no implicit module to use..\n        :return: True if the current user is a member of the group with the\n           given external ID (XML ID), else False.\n        ', kind=None),
                        ),
                        Assert(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='group_ext_id', ctx=Load()),
                                    Compare(
                                        left=Constant(value='.', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='group_ext_id', ctx=Load())],
                                    ),
                                ],
                            ),
                            msg=BinOp(
                                left=Constant(value="External ID '%s' must be fully qualified", kind=None),
                                op=Mod(),
                                right=Name(id='group_ext_id', ctx=Load()),
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='module', ctx=Store()),
                                        Name(id='ext_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='group_ext_id', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='.', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT 1 FROM res_groups_users_rel WHERE uid=%s AND gid IN\n                            (SELECT res_id FROM ir_model_data WHERE module=%s AND name=%s)', kind=None),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_uid',
                                                ctx=Load(),
                                            ),
                                            Name(id='module', ctx=Load()),
                                            Name(id='ext_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='fetchone',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='self._uid', kind=None),
                                Constant(value='group_ext_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='has_group', ctx=Load()),
                            attr='clear_cache',
                            ctx=Store(),
                        ),
                    ],
                    value=Attribute(
                        value=Name(id='_has_group', ctx=Load()),
                        attr='clear_cache',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_action_show',
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
                        Expr(
                            value=Constant(value='If self is a singleton, directly access the form view. If it is a recordset, open a tree view', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.view_users_form', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='res.users', kind=None),
                                    Dict(
                                        keys=[Constant(value='create', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='self', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='views', kind=None),
                                                    Constant(value='domain', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Users', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='list,form', kind=None),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value=None, kind=None),
                                                                    Constant(value='list', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Name(id='view_id', ctx=Load()),
                                                                    Constant(value='form', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='views', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='form', kind=None),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Name(id='view_id', ctx=Load()),
                                                                    Constant(value='form', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_show_groups',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Groups', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='tree,form', kind=None),
                                    Constant(value='res.groups', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='create', kind=None),
                                            Constant(value='delete', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='groups_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='current', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_show_accesses',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Access Rights', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='tree,form', kind=None),
                                    Constant(value='ir.model.access', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='create', kind=None),
                                            Constant(value='delete', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='groups_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='model_access',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='current', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_show_rules',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='target', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Record Rules', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='tree,form', kind=None),
                                    Constant(value='ir.rule', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='create', kind=None),
                                            Constant(value='delete', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='groups_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rule_groups',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='current', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_public',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_public', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_system',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_system', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_admin',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_superuser',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.group_erp_manager', kind=None)],
                                        keywords=[],
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
                    name='_is_superuser',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Name(id='SUPERUSER_ID', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_company_currency_id',
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
                        Return(
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='currency_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_crypt_context',
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
                        Expr(
                            value=Constant(value=' Passlib CryptContext instance used to encrypt and verify\n        passwords. Can be overridden if technical, legal or political matters\n        require different kdfs than the provided default.\n\n        Requires a CryptContext as deprecation and upgrade notices are used\n        internally\n        ', kind=None),
                        ),
                        Return(
                            value=Name(id='DEFAULT_CRYPT_CONTEXT', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_assert_can_auth',
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
                        Expr(
                            value=Constant(value=' Checks that the current environment even allows the current auth\n        request to happen.\n\n        The baseline implementation is a simple linear login cooldown: after\n        a number of failures trying to log-in, the user (by login) is put on\n        cooldown. During the cooldown period, login *attempts* are ignored\n        and logged.\n\n        .. warning::\n\n            The login counter is not shared between workers and not\n            specifically thread-safe, the feature exists mostly for\n            rate-limiting on large number of login attempts (brute-forcing\n            passwords) so that should not be much of an issue.\n\n            For a more complex strategy (e.g. database or distribute storage)\n            override this method. To simply change the cooldown criteria\n            (configuration, ...) override _on_login_cooldown instead.\n\n        .. note::\n\n            This is a *context manager* so it can be called around the login\n            procedure without having to call it itself.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='request', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Yield(value=None),
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='reg', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='registry',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='failures_map', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='reg', ctx=Load()),
                                    Constant(value='_login_failures', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='failures_map', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='failures_map', ctx=Store()),
                                        Attribute(
                                            value=Name(id='reg', ctx=Load()),
                                            attr='_login_failures',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='collections', ctx=Load()),
                                            attr='defaultdict',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                                body=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='datetime', ctx=Load()),
                                                                attr='datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='min',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='remote_addr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='failures', ctx=Store()),
                                        Name(id='previous', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='failures_map', ctx=Load()),
                                slice=Name(id='source', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_on_login_cooldown',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='failures', ctx=Load()),
                                    Name(id='previous', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Login attempt ignored for %s on %s: %d failures since last success, last failure at %s. You can configure the number of login failures before a user is put on cooldown as well as the duration in the System Parameters. Disable this feature by setting "base.login_cooldown_after" to 0.', kind=None),
                                            Name(id='source', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Name(id='failures', ctx=Load()),
                                            Name(id='previous', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='ipaddress', ctx=Load()),
                                                attr='ip_address',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='source', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='is_private',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='The rate-limited IP address %s is classified as private and *might* be a proxy. If your Odoo is behind a proxy, it may be mis-configured. Check that you are running Odoo in Proxy Mode and that the proxy is properly configured, see https://www.odoo.com/documentation/15.0/administration/install/deploy.html#https for details.', kind=None),
                                                    Name(id='source', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessDenied', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Too many login failures, please wait a bit before trying again.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Yield(value=None),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessDenied', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='failures', ctx=Store()),
                                                        Name(id='__', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='reg', ctx=Load()),
                                                    attr='_login_failures',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='source', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='reg', ctx=Load()),
                                                        attr='_login_failures',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='source', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Name(id='failures', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='datetime', ctx=Load()),
                                                                attr='datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='now',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(exc=None, cause=None),
                                    ],
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='reg', ctx=Load()),
                                                attr='_login_failures',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='source', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='contextlib', ctx=Load()),
                            attr='contextmanager',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_on_login_cooldown',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='failures', annotation=None, type_comment=None),
                            arg(arg='previous', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Decides whether the user trying to log in is currently\n        "on cooldown" and not even allowed to attempt logging in.\n\n        The default cooldown function simply puts the user on cooldown for\n        <login_cooldown_duration> seconds after each failure following the\n        <login_cooldown_after>th (0 to disable).\n\n        Can be overridden to implement more complex backoff strategies, or\n        e.g. wind down or reset the cooldown period as the previous failure\n        recedes into the far past.\n\n        :param int failures: number of recorded failures (since last success)\n        :param previous: timestamp of previous failure\n        :type previous:  datetime.datetime\n        :returns: whether the user is currently in cooldown phase (true if cooldown, false if no cooldown and login can continue)\n        :rtype: bool\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='cfg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='min_failures', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cfg', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='base.login_cooldown_after', kind=None),
                                            Constant(value=5, kind=None),
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
                                left=Name(id='min_failures', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='delay', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cfg', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='base.login_cooldown_duration', kind=None),
                                            Constant(value=60, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='failures', ctx=Load()),
                                        ops=[GtE()],
                                        comparators=[Name(id='min_failures', ctx=Load())],
                                    ),
                                    Compare(
                                        left=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Name(id='previous', ctx=Load()),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='timedelta',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='seconds',
                                                        value=Name(id='delay', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                    name='_register_hook',
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
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='check_credentials', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='The check_credentials method of res.users has been renamed _check_credentials. One of your installed modules defines one, but it will not be called anymore.', kind=None)],
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
                    name='_mfa_url',
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
                        Expr(
                            value=Constant(value=' If an MFA method is enabled, returns the URL for its second step. ', kind=None),
                        ),
                        Return(value=None),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='GroupsImplied',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.groups', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='implied_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.groups', kind=None),
                            Constant(value='res_groups_implied_rel', kind=None),
                            Constant(value='gid', kind=None),
                            Constant(value='hid', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Inherits', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Users of this group automatically inherit those groups', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='trans_implied_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.groups', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Transitively inherits', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_trans_implied', kind=None),
                            ),
                            keyword(
                                arg='recursive',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_trans_implied',
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
                        For(
                            target=Name(id='g', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='g', ctx=Load()),
                                            attr='trans_implied_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='g', ctx=Load()),
                                            attr='implied_ids',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='g', ctx=Load()),
                                                attr='implied_ids',
                                                ctx=Load(),
                                            ),
                                            attr='trans_implied_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='implied_ids.trans_implied_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user_ids_list', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='vals', ctx=Load()),
                                        attr='pop',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='users', kind=None),
                                        Constant(value=None, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='vals', ctx=Store()),
                                        iter=Name(id='vals_list', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GroupsImplied', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='group', ctx=Store()),
                                    Name(id='user_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='groups', ctx=Load()),
                                    Name(id='user_ids_list', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Name(id='user_ids', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='group', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='users', kind=None)],
                                                        values=[Name(id='user_ids', ctx=Load())],
                                                    ),
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
                        Return(
                            value=Name(id='groups', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GroupsImplied', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='users', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='implied_ids', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='group', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='\n                    WITH RECURSIVE group_imply(gid, hid) AS (\n                        SELECT gid, hid\n                          FROM res_groups_implied_rel\n                         UNION\n                        SELECT i.gid, r.hid\n                          FROM res_groups_implied_rel r\n                          JOIN group_imply i ON (i.hid = r.gid)\n                    )\n                    INSERT INTO res_groups_users_rel (gid, uid)\n                         SELECT i.hid, r.uid\n                           FROM group_imply i, res_groups_users_rel r\n                          WHERE r.gid = i.gid\n                            AND i.gid = %(gid)s\n                         EXCEPT\n                         SELECT r.gid, r.uid\n                           FROM res_groups_users_rel r\n                           JOIN group_imply i ON (r.gid = i.hid)\n                          WHERE i.gid = %(gid)s\n                ', kind=None),
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='gid',
                                                                value=Attribute(
                                                                    value=Name(id='group', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_one_user_type',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                    name='_apply_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='implied_group', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add the given group to the groups implied by the current group\n        :param implied_group: the implied group to add\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='implied_group', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='implied_ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='implied_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='link',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='implied_group', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                    name='_remove_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='implied_group', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Remove the given group from the implied groups of the current group\n        :param implied_group: the implied group to remove\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='implied_group', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='implied_ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='implied_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='unlink',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='implied_group', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='implied_group', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='users', kind=None)],
                                                values=[
                                                    ListComp(
                                                        elt=Call(
                                                            func=Attribute(
                                                                value=Name(id='Command', ctx=Load()),
                                                                attr='unlink',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='user', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='UsersImplied',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='groups_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='user', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='gs', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='groups_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_origin',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='gs', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='gs', ctx=Load()),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='gs', ctx=Load()),
                                                    attr='trans_implied_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='groups_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Name(id='type', ctx=Load()),
                                                            args=[Name(id='self', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='groups_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='convert_to_write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='gs', ctx=Load()),
                                                    Name(id='user', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UsersImplied', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='users_before', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='u', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='u', ctx=Load()),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.group_user', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UsersImplied', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='groups_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='user', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='has_group',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='base.group_user', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Name(id='user', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='users_before', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='vals', ctx=Store())],
                                                    value=Dict(
                                                        keys=[Constant(value='groups_id', kind=None)],
                                                        values=[
                                                            BinOp(
                                                                left=List(
                                                                    elts=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='Command', ctx=Load()),
                                                                                attr='clear',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='groups_id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='super', ctx=Load()),
                                                                args=[
                                                                    Name(id='UsersImplied', ctx=Load()),
                                                                    Name(id='user', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='vals', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='gs', ctx=Store())],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='concat', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Attribute(
                                                                    value=Name(id='g', ctx=Load()),
                                                                    attr='trans_implied_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='g', ctx=Store()),
                                                                        iter=Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='groups_id',
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
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='vals', ctx=Store())],
                                            value=Dict(
                                                keys=[Constant(value='groups_id', kind=None)],
                                                values=[
                                                    ListComp(
                                                        elt=Call(
                                                            func=Attribute(
                                                                value=Name(id='Command', ctx=Load()),
                                                                attr='link',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='g', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='g', ctx=Store()),
                                                                iter=Name(id='gs', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='super', ctx=Load()),
                                                        args=[
                                                            Name(id='UsersImplied', ctx=Load()),
                                                            Name(id='user', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='vals', ctx=Load())],
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
                        Return(
                            value=Name(id='res', ctx=Load()),
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
            name='GroupsView',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.groups', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GroupsView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_user_groups_view',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='user', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='VIEW_DEPS', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='category_id', kind=None),
                                    Constant(value='implied_ids', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_values0', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='g', ctx=Load()),
                                    slice=Name(id='name', ctx=Load()),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='name', ctx=Store()),
                                        iter=Name(id='VIEW_DEPS', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='values', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                    comprehension(
                                        target=Name(id='g', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GroupsView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_values1', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='g', ctx=Load()),
                                    slice=Name(id='name', ctx=Load()),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='name', ctx=Store()),
                                        iter=Name(id='VIEW_DEPS', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='values', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                    comprehension(
                                        target=Name(id='g', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='view_values0', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='view_values1', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_update_user_groups_view',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                    name='unlink',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GroupsView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_user_groups_view',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                    name='_get_hidden_extra_categories',
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
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='base.module_category_hidden', kind=None),
                                    Constant(value='base.module_category_extra', kind=None),
                                    Constant(value='base.module_category_usability', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_user_groups_view',
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
                        Expr(
                            value=Constant(value=' Modify the view with xmlid ``base.user_groups_view``, which inherits\n            the user form view, and introduces the reified group fields.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.user_groups_view', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='view', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        Compare(
                                            left=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='ir.ui.view', kind=None)],
                                        ),
                                    ],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='install_filename', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='MODULE_UNINSTALL_FLAG', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='xml', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='field',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='groups_id', kind=None),
                                            ),
                                            keyword(
                                                arg='position',
                                                value=Constant(value='after', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='group_no_one', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.group_no_one', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='group_employee', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.group_user', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='xml1', ctx=Store()),
                                                Name(id='xml2', ctx=Store()),
                                                Name(id='xml3', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='xml_by_category', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xml1', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='separator',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='string',
                                                        value=Constant(value='User Type', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='colspan',
                                                        value=Constant(value='2', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='groups',
                                                        value=Constant(value='base.group_no_one', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='user_type_field_name', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='user_type_readonly', ctx=Store())],
                                    value=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Dict(keys=[], values=[])],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sorted_tuples', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_groups_by_application',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='t', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='t', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='xml_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='base.module_category_user_type', kind=None)],
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='app', ctx=Store()),
                                            Name(id='kind', ctx=Store()),
                                            Name(id='gs', ctx=Store()),
                                            Name(id='category_name', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='sorted_tuples', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attrs', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='app', ctx=Load()),
                                                    attr='xml_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_hidden_extra_categories',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attrs', ctx=Load()),
                                                            slice=Constant(value='groups', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='base.group_no_one', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='app', ctx=Load()),
                                                    attr='xml_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='base.module_category_user_type', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='field_name', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='name_selection_groups', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='gs', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='user_type_field_name', ctx=Store())],
                                                    value=Name(id='field_name', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='user_type_readonly', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='readonly', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Name(id='user_type_field_name', ctx=Load()),
                                                                                    Constant(value='!=', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='group_employee', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attrs', ctx=Load()),
                                                            slice=Constant(value='widget', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='radio', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attrs', ctx=Load()),
                                                            slice=Constant(value='groups', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='base.group_no_one', kind=None),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='xml1', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='E', ctx=Load()),
                                                                    attr='field',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='name',
                                                                        value=Name(id='field_name', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg=None,
                                                                        value=Name(id='attrs', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='xml1', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='E', ctx=Load()),
                                                                    attr='newline',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
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
                                                        left=Name(id='kind', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='selection', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='field_name', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='name_selection_groups', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='gs', ctx=Load()),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='attrs', ctx=Load()),
                                                                    slice=Constant(value='attrs', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='user_type_readonly', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='category_name', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='xml_by_category', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='xml_by_category', ctx=Load()),
                                                                            slice=Name(id='category_name', ctx=Load()),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=List(elts=[], ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='xml_by_category', ctx=Load()),
                                                                                slice=Name(id='category_name', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='E', ctx=Load()),
                                                                                    attr='newline',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
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
                                                                    value=Subscript(
                                                                        value=Name(id='xml_by_category', ctx=Load()),
                                                                        slice=Name(id='category_name', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='E', ctx=Load()),
                                                                            attr='field',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='name',
                                                                                value=Name(id='field_name', ctx=Load()),
                                                                            ),
                                                                            keyword(
                                                                                arg=None,
                                                                                value=Name(id='attrs', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='xml_by_category', ctx=Load()),
                                                                        slice=Name(id='category_name', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='E', ctx=Load()),
                                                                            attr='newline',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='app_name', ctx=Store())],
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='app', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='Other', kind=None),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='xml3', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='E', ctx=Load()),
                                                                            attr='separator',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='string',
                                                                                value=Name(id='app_name', ctx=Load()),
                                                                            ),
                                                                            keyword(
                                                                                arg='colspan',
                                                                                value=Constant(value='4', kind=None),
                                                                            ),
                                                                            keyword(
                                                                                arg=None,
                                                                                value=Name(id='attrs', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='attrs', ctx=Load()),
                                                                    slice=Constant(value='attrs', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='user_type_readonly', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='g', ctx=Store()),
                                                            iter=Name(id='gs', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='field_name', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='name_boolean_group', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='g', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='g', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='group_no_one', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='xml3', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='E', ctx=Load()),
                                                                                            attr='field',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='name',
                                                                                                value=Name(id='field_name', ctx=Load()),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='invisible',
                                                                                                value=Constant(value='1', kind=None),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg=None,
                                                                                                value=Name(id='attrs', ctx=Load()),
                                                                                            ),
                                                                                        ],
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
                                                                                    value=Name(id='xml3', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='E', ctx=Load()),
                                                                                            attr='field',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='name',
                                                                                                value=Name(id='field_name', ctx=Load()),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg=None,
                                                                                                value=Name(id='attrs', ctx=Load()),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xml3', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='class', kind=None)],
                                                values=[Constant(value='o_label_nowrap', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='user_type_field_name', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='user_type_attrs', ctx=Store())],
                                            value=Dict(
                                                keys=[Constant(value='invisible', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='user_type_field_name', ctx=Load()),
                                                                    Constant(value='!=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='group_employee', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='user_type_attrs', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                For(
                                    target=Name(id='xml_cat', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='xml_by_category', ctx=Load()),
                                                    attr='keys',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='it', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Subscript(
                                                        value=Name(id='it', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='master_category_name', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='xml_cat', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='xml2', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Starred(
                                                                value=Subscript(
                                                                    value=Name(id='xml_by_category', ctx=Load()),
                                                                    slice=Name(id='xml_cat', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='col',
                                                                value=Constant(value='2', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='string',
                                                                value=Name(id='master_category_name', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='xml', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='field',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=Name(id='xml1', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='col',
                                                        value=Constant(value='2', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=Name(id='xml2', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='col',
                                                        value=Constant(value='2', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='attrs',
                                                        value=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='user_type_attrs', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=Name(id='xml3', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='col',
                                                        value=Constant(value='4', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='attrs',
                                                        value=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='user_type_attrs', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='groups_id', kind=None),
                                            ),
                                            keyword(
                                                arg='position',
                                                value=Constant(value='replace', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xml', ctx=Load()),
                                            attr='addprevious',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='Comment',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='GENERATED AUTOMATICALLY BY GROUPS', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='xml_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='tostring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xml', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='pretty_print',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='encoding',
                                        value=Constant(value='unicode', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='xml_content', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='view', ctx=Load()),
                                        attr='arch',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_context', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='new_context', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='install_filename', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='new_context', ctx=Load()),
                                            slice=Constant(value='lang', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='view', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='new_context', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='arch', kind=None)],
                                                values=[Name(id='xml_content', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_application_groups',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the non-share groups that satisfy ``domain``. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='domain', ctx=Load()),
                                        op=Add(),
                                        right=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='share', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                    name='get_groups_by_application',
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
                        Expr(
                            value=Constant(value=" Return all groups classified by application (module category), as a list::\n\n                [(app, kind, groups), ...],\n\n            where ``app`` and ``groups`` are recordsets, and ``kind`` is either\n            ``'boolean'`` or ``'selection'``. Applications are given in sequence\n            order.  If ``kind`` is ``'selection'``, ``groups`` are given in\n            reverse implication order.\n        ", kind=None),
                        ),
                        FunctionDef(
                            name='linearize',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='app', annotation=None, type_comment=None),
                                    arg(arg='gs', annotation=None, type_comment=None),
                                    arg(arg='category_name', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='app', ctx=Load()),
                                            attr='xml_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='base.module_category_user_type', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='app', ctx=Load()),
                                                    Constant(value='selection', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='gs', ctx=Load()),
                                                            attr='sorted',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='category_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='order', ctx=Store())],
                                    value=DictComp(
                                        key=Name(id='g', ctx=Load()),
                                        value=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Attribute(
                                                        value=Name(id='g', ctx=Load()),
                                                        attr='trans_implied_ids',
                                                        ctx=Load(),
                                                    ),
                                                    op=BitAnd(),
                                                    right=Name(id='gs', ctx=Load()),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='g', ctx=Store()),
                                                iter=Name(id='gs', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='app', ctx=Load()),
                                            attr='xml_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='base.module_category_accounting_accounting', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='app', ctx=Load()),
                                                    Constant(value='selection', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='gs', ctx=Load()),
                                                            attr='sorted',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='key',
                                                                value=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='category_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='values',
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
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='gs', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='app', ctx=Load()),
                                                    Constant(value='selection', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='gs', ctx=Load()),
                                                            attr='sorted',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='key',
                                                                value=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='category_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='app', ctx=Load()),
                                                    Constant(value='boolean', kind=None),
                                                    Name(id='gs', ctx=Load()),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=100, kind=None),
                                                            Constant(value='Other', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='by_app', ctx=Store()),
                                        Name(id='others', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='defaultdict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='g', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_application_groups',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='g', ctx=Load()),
                                        attr='category_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='by_app', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='g', ctx=Load()),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='g', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='others', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='g', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='app', ctx=Store()),
                                    Name(id='gs', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='by_app', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='it', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='it', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='sequence',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='app', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='linearize', ctx=Load()),
                                                        args=[
                                                            Name(id='app', ctx=Load()),
                                                            Name(id='gs', ctx=Load()),
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='app', ctx=Load()),
                                                                            attr='parent_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='sequence',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='app', ctx=Load()),
                                                                            attr='parent_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='linearize', ctx=Load()),
                                                        args=[
                                                            Name(id='app', ctx=Load()),
                                                            Name(id='gs', ctx=Load()),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=100, kind=None),
                                                                    Constant(value='Other', kind=None),
                                                                ],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='others', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.module.category', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='boolean', kind=None),
                                                    Name(id='others', ctx=Load()),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=100, kind=None),
                                                            Constant(value='Other', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ModuleCategory',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.module.category', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='name', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.groups', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_update_user_groups_view',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                    name='unlink',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.groups', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_update_user_groups_view',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
            name='UsersView',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='new_vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_remove_reified_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UsersView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='new_vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_multi_company_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_multi_company', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='group_multi_company_id', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='user', ctx=Store()),
                                    iter=Name(id='users', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='company_ids',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[LtE()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='group_multi_company_id', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='groups_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
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
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='groups_id', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='unlink',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='group_multi_company_id', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='company_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='group_multi_company_id', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='groups_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ids',
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
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[Constant(value='groups_id', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='Command', ctx=Load()),
                                                                                            attr='link',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='group_multi_company_id', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
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
                        Return(
                            value=Name(id='users', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_remove_reified_groups',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UsersView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='company_ids', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='group_multi_company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='base.group_multi_company', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='group_multi_company', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='user', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='company_ids',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[LtE()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='group_multi_company', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
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
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='groups_id', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='unlink',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='group_multi_company', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='company_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='group_multi_company', ctx=Load()),
                                                                            attr='users',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ids',
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
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[Constant(value='groups_id', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='Command', ctx=Load()),
                                                                                            attr='link',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='group_multi_company', ctx=Load()),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
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
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='new',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='origin', annotation=None, type_comment=None),
                            arg(arg='ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Dict(keys=[], values=[]),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_remove_reified_groups',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='values',
                                        value=Name(id='values', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='origin',
                                        value=Name(id='origin', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='ref',
                                        value=Name(id='ref', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_multi_company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='base.group_multi_company', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='group_multi_company', ctx=Load()),
                                    Compare(
                                        left=Constant(value='company_ids', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='company_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[LtE()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='group_multi_company', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
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
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='groups_id', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Command', ctx=Load()),
                                                                            attr='unlink',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='group_multi_company', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='company_ids',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='group_multi_company', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
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
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='groups_id', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='link',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='group_multi_company', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='user', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_remove_reified_groups',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' return `values` without reified group fields ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='add', ctx=Store()),
                                        Name(id='rem', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    List(elts=[], ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values1', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='val', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='is_boolean_group', ctx=Load()),
                                        args=[Name(id='key', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=IfExp(
                                                        test=Name(id='val', ctx=Load()),
                                                        body=Name(id='add', ctx=Load()),
                                                        orelse=Name(id='rem', ctx=Load()),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='get_boolean_group', ctx=Load()),
                                                        args=[Name(id='key', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='is_selection_groups', ctx=Load()),
                                                args=[Name(id='key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='rem', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Name(id='get_selection_groups', ctx=Load()),
                                                        args=[Name(id='key', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=Name(id='val', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='add', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='val', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values1', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='val', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='groups_id', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='add', ctx=Load()),
                                            Name(id='rem', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values1', ctx=Load()),
                                            slice=Constant(value='groups_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='itertools', ctx=Load()),
                                                    attr='chain',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='zip', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='repeat', ctx=Load()),
                                                                args=[Constant(value=3, kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Name(id='rem', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='zip', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='repeat', ctx=Load()),
                                                                args=[Constant(value=4, kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Name(id='add', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values1', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
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
                                Tuple(
                                    elts=[
                                        Name(id='group_fields', ctx=Store()),
                                        Name(id='fields', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='partition', ctx=Load()),
                                args=[
                                    Name(id='is_reified_group', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fields1', ctx=Store())],
                            value=IfExp(
                                test=Name(id='group_fields', ctx=Load()),
                                body=BinOp(
                                    left=Name(id='fields', ctx=Load()),
                                    op=Add(),
                                    right=List(
                                        elts=[Constant(value='groups_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Name(id='fields', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UsersView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields1', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_reified_groups',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='group_fields', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='field_onchange', annotation=None, type_comment=None),
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
                                    value=Name(id='field_onchange', ctx=Load()),
                                    slice=Constant(value='groups_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='onchange',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='values', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='field_onchange', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='field_name', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_reified_groups',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='filter', ctx=Load()),
                                                args=[
                                                    Name(id='is_reified_group', ctx=Load()),
                                                    Name(id='field_onchange', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='value', kind=None),
                                                    Dict(keys=[], values=[]),
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
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='load', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='_classic_read', kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fields1', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='fields', ctx=Load()),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='fields_get',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='group_fields', ctx=Store()),
                                        Name(id='other_fields', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='partition', ctx=Load()),
                                args=[
                                    Name(id='is_reified_group', ctx=Load()),
                                    Name(id='fields1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='drop_groups_id', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='group_fields', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='groups_id', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='other_fields', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='other_fields', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='groups_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='drop_groups_id', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='other_fields', ctx=Store())],
                                    value=Name(id='fields', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UsersView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[Name(id='other_fields', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='load',
                                        value=Name(id='load', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='group_fields', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='values', ctx=Store()),
                                    iter=Name(id='res', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_add_reified_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='group_fields', ctx=Load()),
                                                    Name(id='values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Name(id='drop_groups_id', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='groups_id', kind=None),
                                                            Constant(value=None, kind=None),
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
                            orelse=[],
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
                    name='_add_reified_groups',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' add the given reified group fields into `values` ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='gids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='parse_m2m', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='groups_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='f', ctx=Store()),
                            iter=Name(id='fields', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='is_boolean_group', ctx=Load()),
                                        args=[Name(id='f', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Name(id='f', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Compare(
                                                left=Call(
                                                    func=Name(id='get_boolean_group', ctx=Load()),
                                                    args=[Name(id='f', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='gids', ctx=Load())],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='is_selection_groups', ctx=Load()),
                                                args=[Name(id='f', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='sel_groups', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='res.groups', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='get_selection_groups', ctx=Load()),
                                                                args=[Name(id='f', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='sel_order', ctx=Store())],
                                                    value=DictComp(
                                                        key=Name(id='g', ctx=Load()),
                                                        value=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='g', ctx=Load()),
                                                                        attr='trans_implied_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=BitAnd(),
                                                                    right=Name(id='sel_groups', ctx=Load()),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='g', ctx=Store()),
                                                                iter=Name(id='sel_groups', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='sel_groups', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sel_groups', ctx=Load()),
                                                            attr='sorted',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='key',
                                                                value=Attribute(
                                                                    value=Name(id='sel_order', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='selected', ctx=Store())],
                                                    value=ListComp(
                                                        elt=Name(id='gid', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='gid', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='sel_groups', ctx=Load()),
                                                                    attr='ids',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Name(id='gid', ctx=Load()),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='gids', ctx=Load())],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='ref',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='base.group_user', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='selected', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Name(id='f', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ref',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='base.group_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Name(id='f', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='selected', ctx=Load()),
                                                                            Subscript(
                                                                                value=Name(id='selected', ctx=Load()),
                                                                                slice=UnaryOp(
                                                                                    op=USub(),
                                                                                    operand=Constant(value=1, kind=None),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fields_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='allfields', annotation=None, type_comment=None),
                            arg(arg='attributes', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UsersView', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='fields_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='allfields', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='attributes',
                                        value=Name(id='attributes', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='app', ctx=Store()),
                                    Name(id='kind', ctx=Store()),
                                    Name(id='gs', ctx=Store()),
                                    Name(id='category_name', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.groups', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_groups_by_application',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='kind', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='selection', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='selection_vals', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='app', ctx=Load()),
                                                    attr='xml_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='base.module_category_user_type', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='selection_vals', ctx=Store())],
                                                    value=List(elts=[], ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='field_name', ctx=Store())],
                                            value=Call(
                                                func=Name(id='name_selection_groups', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='gs', ctx=Load()),
                                                        attr='ids',
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
                                                    Name(id='allfields', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='field_name', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='allfields', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='tips', ctx=Store())],
                                            value=ListComp(
                                                elt=BinOp(
                                                    left=Constant(value='%s: %s', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='g', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='g', ctx=Load()),
                                                                attr='comment',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='g', ctx=Store()),
                                                        iter=Name(id='gs', ctx=Load()),
                                                        ifs=[
                                                            Attribute(
                                                                value=Name(id='g', ctx=Load()),
                                                                attr='comment',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Name(id='field_name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='selection', kind=None),
                                                    Constant(value='help', kind=None),
                                                    Constant(value='exportable', kind=None),
                                                    Constant(value='selectable', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='selection', kind=None),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='app', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Other', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    BinOp(
                                                        left=Name(id='selection_vals', ctx=Load()),
                                                        op=Add(),
                                                        right=ListComp(
                                                            elt=Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='g', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='g', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='g', ctx=Store()),
                                                                    iter=Name(id='gs', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Constant(value='\n', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tips', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        For(
                                            target=Name(id='g', ctx=Store()),
                                            iter=Name(id='gs', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='field_name', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='name_boolean_group', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='g', ctx=Load()),
                                                                attr='id',
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
                                                            Name(id='allfields', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='field_name', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='allfields', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Name(id='field_name', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='string', kind=None),
                                                            Constant(value='help', kind=None),
                                                            Constant(value='exportable', kind=None),
                                                            Constant(value='selectable', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='boolean', kind=None),
                                                            Attribute(
                                                                value=Name(id='g', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='g', ctx=Load()),
                                                                attr='comment',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='CheckIdentity',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Wizard used to re-check the user's credentials (password)\n\n    Might be useful before the more security-sensitive operations, users might be\n    leaving their computer unlocked & unattended. Re-checking credentials mitigates\n    some of the risk of a third party using such an unattended device to manipulate\n    the account.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='res.users.identitycheck', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Password Check Wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='request', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Attribute(
                                    value=Name(id='fields', ctx=Load()),
                                    attr='NO_ACCESS',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='password', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='run_check',
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
                        Assert(
                            test=Name(id='request', ctx=Load()),
                            msg=Constant(value='This method can only be accessed over HTTP', kind=None),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='create_uid',
                                                ctx=Load(),
                                            ),
                                            attr='_check_credentials',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='password',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='interactive', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessDenied', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Incorrect Password, try again or click on Forgot Password to reset your password.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='password',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='identity-check-last', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='ctx', ctx=Store()),
                                        Name(id='model', ctx=Store()),
                                        Name(id='ids', ctx=Store()),
                                        Name(id='method', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='request',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='context',
                                                                value=Name(id='ctx', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    slice=Name(id='model', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Name(id='method', ctx=Load()),
                                    ],
                                    keywords=[],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ChangePasswordWizard',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" A wizard to manage the change of users' passwords. ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='change.password.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Change Password Wizard', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_user_ids',
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
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_context',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='active_model', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='res.users', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='active_ids', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='Command', ctx=Load()),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='user_id', kind=None),
                                                Constant(value='user_login', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='login',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='user', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.users', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='user_ids', ctx=Load())],
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
                Assign(
                    targets=[Name(id='user_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='change.password.user', kind=None),
                            Constant(value='wizard_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Users', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_user_ids', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='change_password_button',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_ids',
                                        ctx=Load(),
                                    ),
                                    attr='change_password_button',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_ids',
                                            ctx=Load(),
                                        ),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='tag', kind=None),
                                        ],
                                        values=[
                                            Constant(value='ir.actions.client', kind=None),
                                            Constant(value='reload', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='type', kind=None)],
                                values=[Constant(value='ir.actions.act_window_close', kind=None)],
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
            name='ChangePasswordUser',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A model to configure users in the change password wizard. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='change.password.user', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='User, Change Password Wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='wizard_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='change.password.wizard', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Wizard', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='User', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_login', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='User Login', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_passwd', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='New Password', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='change_password_button',
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
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='new_passwd',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="Before clicking on 'Change Password', you have to write a new password.", kind=None)],
                                                        keywords=[],
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
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='user_id',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='password', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='new_passwd',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='new_passwd', kind=None)],
                                        values=[Constant(value=False, kind=None)],
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
            targets=[Name(id='API_KEY_SIZE', ctx=Store())],
            value=Constant(value=20, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='INDEX_SIZE', ctx=Store())],
            value=Constant(value=8, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='KEY_CRYPT_CONTEXT', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='passlib', ctx=Load()),
                        attr='context',
                        ctx=Load(),
                    ),
                    attr='CryptContext',
                    ctx=Load(),
                ),
                args=[
                    List(
                        elts=[Constant(value='pbkdf2_sha512', kind=None)],
                        ctx=Load(),
                    ),
                ],
                keywords=[
                    keyword(
                        arg='pbkdf2_sha512__rounds',
                        value=Constant(value=6000, kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='hash_api_key', ctx=Store())],
            value=BoolOp(
                op=Or(),
                values=[
                    Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='KEY_CRYPT_CONTEXT', ctx=Load()),
                            Constant(value='hash', kind=None),
                            Constant(value=None, kind=None),
                        ],
                        keywords=[],
                    ),
                    Attribute(
                        value=Name(id='KEY_CRYPT_CONTEXT', ctx=Load()),
                        attr='encrypt',
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='APIKeysUser',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='api_key_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users.apikeys', kind=None),
                            Constant(value='user_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='API Keys', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='SELF_READABLE_FIELDS',
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
                        Return(
                            value=BinOp(
                                left=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='SELF_READABLE_FIELDS',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=List(
                                    elts=[Constant(value='api_key_ids', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='SELF_WRITEABLE_FIELDS',
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
                        Return(
                            value=BinOp(
                                left=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='SELF_WRITEABLE_FIELDS',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=List(
                                    elts=[Constant(value='api_key_ids', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_rpc_api_keys_only',
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
                        Expr(
                            value=Constant(value=' To be overridden if RPC access needs to be restricted to API keys, e.g. for 2FA ', kind=None),
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
                    name='_check_credentials',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='user_agent_env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user_agent_env', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='user_agent_env', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='user_agent_env', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='interactive', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='interactive', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='user_agent_env', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="_check_credentials without 'interactive' env key, assuming interactive login.                     Check calls and overrides to ensure the 'interactive' key is properly set in                     all _check_credentials environments", kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_check_credentials',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='password', ctx=Load()),
                                            Name(id='user_agent_env', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='_rpc_api_keys_only',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='super', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='_check_credentials',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='password', ctx=Load()),
                                                    Name(id='user_agent_env', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='AccessDenied', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users.apikeys', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_check_credentials',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='scope',
                                            value=Constant(value='rpc', kind=None),
                                        ),
                                        keyword(
                                            arg='key',
                                            value=Name(id='password', ctx=Load()),
                                        ),
                                    ],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='AccessDenied', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='api_key_wizard',
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='views', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='res.users.apikeys.description', kind=None),
                                    Constant(value='New API Key', kind=None),
                                    Constant(value='new', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='check_identity', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='APIKeys',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[
                        Name(id='_name', ctx=Store()),
                        Name(id='_description', ctx=Store()),
                    ],
                    value=Constant(value='res.users.apikeys', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='scope', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Scope', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='create_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Creation Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value="\n        CREATE TABLE IF NOT EXISTS {table} (\n            id serial primary key,\n            name varchar not null,\n            user_id integer not null REFERENCES res_users(id),\n            scope varchar,\n            index varchar({index_size}) not null CHECK (char_length(index) = {index_size}),\n            key varchar not null,\n            create_date timestamp without time zone DEFAULT (now() at time zone 'utc')\n        )\n        ", kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='table',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_table',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='index_size',
                                                value=Name(id='INDEX_SIZE', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='index_name', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_table',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Constant(value='_user_id_index_idx', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='index_name', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=63, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='index_name', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_table',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=50, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value='_idx_', kind=None),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='sha256', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_table',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='hexdigest',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=8, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='\n        CREATE INDEX IF NOT EXISTS {index_name} ON {table} (user_id, index);\n        ', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='table',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_table',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='index_name',
                                                value=Name(id='index_name', ctx=Load()),
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
                    name='remove',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_remove',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='check_identity', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_remove',
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
                        Expr(
                            value=Constant(value="Use the remove() method to remove an API Key. This method implement logic,\n        but won't check the identity (mainly used to remove trusted devices)", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='type', kind=None)],
                                        values=[Constant(value='ir.actions.act_window_close', kind=None)],
                                    ),
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='is_system',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='user_id', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ip', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='request', ctx=Load()),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='environ',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='REMOTE_ADDR', kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value='n/a', kind=None),
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
                                            Constant(value="API key(s) removed: scope: <%s> for '%s' (#%s) from %s", kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='scope', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='login',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                            Name(id='ip', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='type', kind=None)],
                                        values=[Constant(value='ir.actions.act_window_close', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='AccessError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value="You can not remove API keys unless they're yours or you are a system user", kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_credentials',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[
                            arg(arg='scope', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        kw_defaults=[
                            None,
                            None,
                        ],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Name(id='scope', ctx=Load()),
                            msg=Constant(value='scope is required', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='index', ctx=Store())],
                            value=Subscript(
                                value=Name(id='key', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=Name(id='INDEX_SIZE', ctx=Load()),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='\n            SELECT user_id, key\n            FROM {} INNER JOIN res_users u ON (u.id = user_id)\n            WHERE u.active and index = %s AND (scope IS NULL OR scope = %s)\n        ', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_table',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='index', ctx=Load()),
                                            Name(id='scope', ctx=Load()),
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
                                    Name(id='user_id', ctx=Store()),
                                    Name(id='current_key', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='KEY_CRYPT_CONTEXT', ctx=Load()),
                                            attr='verify',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='key', ctx=Load()),
                                            Name(id='current_key', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='user_id', ctx=Load()),
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
                    name='_generate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scope', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generates an api key.\n        :param str scope: the scope of the key. If None, the key will give access to any rpc.\n        :param str name: the name of the key, mainly intended to be displayed in the UI.\n        :return: str: the key.\n\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='k', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='binascii', ctx=Load()),
                                            attr='hexlify',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='urandom',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='API_KEY_SIZE', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='\n        INSERT INTO {table} (name, user_id, scope, key, index)\n        VALUES (%s, %s, %s, %s, %s)\n        RETURNING id\n        ', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='table',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_table',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='name', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='scope', ctx=Load()),
                                            Call(
                                                func=Name(id='hash_api_key', ctx=Load()),
                                                args=[Name(id='k', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Name(id='k', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Name(id='INDEX_SIZE', ctx=Load()),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ip', ctx=Store())],
                            value=IfExp(
                                test=Name(id='request', ctx=Load()),
                                body=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='REMOTE_ADDR', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Constant(value='n/a', kind=None),
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
                                    Constant(value="%s generated: scope: <%s> for '%s' (#%s) from %s", kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_description',
                                        ctx=Load(),
                                    ),
                                    Name(id='scope', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='login',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Name(id='ip', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='k', ctx=Load()),
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
            name='APIKeyDescription',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[
                        Name(id='_name', ctx=Store()),
                        Name(id='_description', ctx=Store()),
                    ],
                    value=Constant(value='res.users.apikeys.description', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='make_key',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_has_groups',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.group_user', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Only internal users can create API keys', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='description', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='k', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users.apikeys', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_generate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=None, kind=None),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='description', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='res.users.apikeys.show', kind=None),
                                    Constant(value='API Key Ready', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='new', kind=None),
                                    Dict(
                                        keys=[Constant(value='default_key', kind=None)],
                                        values=[Name(id='k', ctx=Load())],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='check_identity', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='APIKeyShow',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[
                        Name(id='_name', ctx=Store()),
                        Name(id='_description', ctx=Store()),
                    ],
                    value=Constant(value='res.users.apikeys.show', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Id',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
