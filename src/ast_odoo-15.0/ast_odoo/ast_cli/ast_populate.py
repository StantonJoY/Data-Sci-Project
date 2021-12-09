Module(
    body=[
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='fnmatch', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='optparse', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
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
        ClassDef(
            name='Populate',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cmdargs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parser', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                attr='parser',
                                ctx=Load(),
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
                                    Constant(value='Populate Configuration', kind=None),
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
                                args=[Constant(value='--size', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='population_size', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Populate database with auto-generated data. Value should be the population size: small, medium or large', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Constant(value='small', kind=None),
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
                                args=[Constant(value='--models', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='populate_models', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Comma separated list of model or pattern (fnmatch)', kind=None),
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
                            targets=[Name(id='opt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    attr='parse_config',
                                    ctx=Load(),
                                ),
                                args=[Name(id='cmdargs', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='populate_models', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='opt', ctx=Load()),
                                        attr='populate_models',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='opt', ctx=Load()),
                                                        attr='populate_models',
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=',', kind=None)],
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
                            targets=[Name(id='population_size', ctx=Store())],
                            value=Attribute(
                                value=Name(id='opt', ctx=Load()),
                                attr='population_size',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dbname', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='db_name', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dbname', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
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
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='api',
                                                ctx=Load(),
                                            ),
                                            attr='Environment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='SUPERUSER_ID',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='populate',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='env', ctx=Load()),
                                            Name(id='population_size', ctx=Load()),
                                            Name(id='populate_models', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='populate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                            arg(arg='model_patterns', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Attribute(
                                value=Name(id='env', ctx=Load()),
                                attr='registry',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='populated_models', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='populated_models',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ordered_models', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_get_ordered_models',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='env', ctx=Load()),
                                            Name(id='model_patterns', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='log',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=25, kind=None),
                                            Constant(value='Populating database', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='model', ctx=Store()),
                                    iter=Name(id='ordered_models', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Populating database for model %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='t0', ctx=Store())],
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
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='registry', ctx=Load()),
                                                        attr='populated_models',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='_populate',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='size', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='env', ctx=Load()),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='commit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='model_time', ctx=Store())],
                                            value=BinOp(
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
                                                right=Name(id='t0', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='model_time', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Populated database for model %s (total: %fs) (average: %fms per record)', kind=None),
                                                            Attribute(
                                                                value=Name(id='model', ctx=Load()),
                                                                attr='_name',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='model_time', ctx=Load()),
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='model_time', ctx=Load()),
                                                                    op=Div(),
                                                                    right=Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='registry', ctx=Load()),
                                                                                    attr='populated_models',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Attribute(
                                                                                    value=Name(id='model', ctx=Load()),
                                                                                    attr='_name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                op=Mult(),
                                                                right=Constant(value=1000, kind=None),
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
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Something went wrong populating database', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[
                                Assign(
                                    targets=[Name(id='populated_models', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='registry', ctx=Load()),
                                        attr='populated_models',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Delete(
                                    targets=[
                                        Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='populated_models',
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='populated_models', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_ordered_models',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='model_patterns', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Computing model order', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='processed', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ordered_models', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='visited', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='add_model',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='model', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='processed', ctx=Load())],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='model', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='visited', ctx=Load())],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValueError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Cyclic dependency detected for %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='model', ctx=Load()),
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
                                                    value=Name(id='visited', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='model', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        For(
                                            target=Name(id='dep', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_populate_dependencies',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='add_model', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Name(id='dep', ctx=Load()),
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ordered_models', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='model', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='processed', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='model', ctx=Load())],
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
                        For(
                            target=Name(id='model', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ir_model', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.model', kind=None),
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
                                                            Constant(value='model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='model', ctx=Load()),
                                                                attr='_name',
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='model_patterns', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='any', ctx=Load()),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Call(
                                                                func=Attribute(
                                                                    value=Name(id='fnmatch', ctx=Load()),
                                                                    attr='fnmatch',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='model', ctx=Load()),
                                                                        attr='_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='match', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='match', ctx=Store()),
                                                                    iter=Name(id='model_patterns', ctx=Load()),
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
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_transient',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_abstract',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='model_patterns', ctx=Load()),
                                            ),
                                            Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Call(
                                                            func=Attribute(
                                                                value=Name(id='module', ctx=Load()),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='test_', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='module', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='ir_model', ctx=Load()),
                                                                            attr='modules',
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
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='add_model', ctx=Load()),
                                        args=[Name(id='model', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='ordered_models', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
