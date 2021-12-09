Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='difflib', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='can_import', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_module_resource', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='mute_logger', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base_import.models.base_import',
            names=[alias(name='ImportValidationError', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='ID_FIELD', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='id', kind=None),
                    Constant(value='name', kind=None),
                    Constant(value='string', kind=None),
                    Constant(value='required', kind=None),
                    Constant(value='fields', kind=None),
                    Constant(value='type', kind=None),
                ],
                values=[
                    Constant(value='id', kind=None),
                    Constant(value='id', kind=None),
                    Constant(value='External ID', kind=None),
                    Constant(value=False, kind=None),
                    List(elts=[], ctx=Load()),
                    Constant(value='id', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='make_field',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='name', annotation=None, type_comment=None),
                    arg(arg='string', annotation=None, type_comment=None),
                    arg(arg='required', annotation=None, type_comment=None),
                    arg(arg='fields', annotation=None, type_comment=None),
                    arg(arg='field_type', annotation=None, type_comment=None),
                    arg(arg='model_name', annotation=None, type_comment=None),
                    arg(arg='comodel_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='value', kind=None),
                    Constant(value='Value', kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value='id', kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                If(
                    test=Compare(
                        left=Name(id='fields', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='field', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='id', kind=None),
                            Constant(value='name', kind=None),
                            Constant(value='string', kind=None),
                            Constant(value='required', kind=None),
                            Constant(value='fields', kind=None),
                            Constant(value='type', kind=None),
                        ],
                        values=[
                            Name(id='name', ctx=Load()),
                            Name(id='name', ctx=Load()),
                            Name(id='string', ctx=Load()),
                            Name(id='required', ctx=Load()),
                            Name(id='fields', ctx=Load()),
                            Name(id='field_type', ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='model_name', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field', ctx=Load()),
                                    slice=Constant(value='model_name', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='model_name', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Name(id='comodel_name', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field', ctx=Load()),
                                    slice=Constant(value='comodel_name', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='comodel_name', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=List(
                        elts=[
                            Name(id='ID_FIELD', ctx=Load()),
                            Name(id='field', ctx=Load()),
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
            name='sorted_fields',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='fields', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' recursively sort field lists to ease comparison ', kind=None),
                ),
                Assign(
                    targets=[Name(id='recursed', ctx=Store())],
                    value=ListComp(
                        elt=Call(
                            func=Name(id='dict', ctx=Load()),
                            args=[Name(id='field', ctx=Load())],
                            keywords=[
                                keyword(
                                    arg='fields',
                                    value=Call(
                                        func=Name(id='sorted_fields', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='field', ctx=Load()),
                                                slice=Constant(value='fields', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='field', ctx=Store()),
                                iter=Name(id='fields', ctx=Load()),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='sorted', ctx=Load()),
                        args=[Name(id='recursed', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='key',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='field', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Subscript(
                                        value=Name(id='field', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
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
        ClassDef(
            name='BaseImportCase',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='assertEqualFields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields1', annotation=None, type_comment=None),
                            arg(arg='fields2', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='f1', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted_fields', ctx=Load()),
                                args=[Name(id='fields1', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f2', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted_fields', ctx=Load()),
                                args=[Name(id='fields2', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='f1', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='f2', ctx=Load())],
                            ),
                            msg=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='difflib', ctx=Load()),
                                            attr='unified_diff',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='pprint', ctx=Load()),
                                                            attr='pformat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='f1', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='splitlines',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='pprint', ctx=Load()),
                                                            attr='pformat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='f2', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='splitlines',
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
            name='TestBasicFields',
            bases=[Name(id='BaseImportCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='get_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_fields_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='base_import.tests.models.', kind=None),
                                        op=Add(),
                                        right=Name(id='field', ctx=Load()),
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
                    name='test_base',
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
                            value=Constant(value=' A basic field is not required ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='char', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='make_field', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='field_type',
                                                value=Constant(value='char', kind=None),
                                            ),
                                            keyword(
                                                arg='model_name',
                                                value=Constant(value='base_import.tests.models.char', kind=None),
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
                    name='test_required',
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
                            value=Constant(value=' Required fields should be flagged (so they can be fill-required) ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='char.required', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='make_field', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='required',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='field_type',
                                                value=Constant(value='char', kind=None),
                                            ),
                                            keyword(
                                                arg='model_name',
                                                value=Constant(value='base_import.tests.models.char.required', kind=None),
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
                    name='test_readonly',
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
                            value=Constant(value=' Readonly fields should be filtered out', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='char.readonly', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Name(id='ID_FIELD', ctx=Load())],
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
                    name='test_readonly_states',
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
                            value=Constant(value=' Readonly fields with states should not be filtered out', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='char.states', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='make_field', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='field_type',
                                                value=Constant(value='char', kind=None),
                                            ),
                                            keyword(
                                                arg='model_name',
                                                value=Constant(value='base_import.tests.models.char.states', kind=None),
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
                    name='test_readonly_states_noreadonly',
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
                            value=Constant(value=' Readonly fields with states having nothing to do with\n        readonly should still be filtered out', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='char.noreadonly', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Name(id='ID_FIELD', ctx=Load())],
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
                    name='test_readonly_states_stillreadonly',
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
                            value=Constant(value=' Readonly fields with readonly states leaving them readonly\n        always... filtered out', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='char.stillreadonly', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Name(id='ID_FIELD', ctx=Load())],
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
                    name='test_m2o',
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
                            value=Constant(value=' M2O fields should allow import of themselves (name_get),\n        their id and their xid', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='m2o', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='make_field', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='field_type',
                                                value=Constant(value='many2one', kind=None),
                                            ),
                                            keyword(
                                                arg='comodel_name',
                                                value=Constant(value='base_import.tests.models.m2o.related', kind=None),
                                            ),
                                            keyword(
                                                arg='model_name',
                                                value=Constant(value='base_import.tests.models.m2o', kind=None),
                                            ),
                                            keyword(
                                                arg='fields',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='id', kind=None),
                                                                Constant(value='name', kind=None),
                                                                Constant(value='string', kind=None),
                                                                Constant(value='required', kind=None),
                                                                Constant(value='fields', kind=None),
                                                                Constant(value='type', kind=None),
                                                                Constant(value='model_name', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='id', kind=None),
                                                                Constant(value='External ID', kind=None),
                                                                Constant(value=False, kind=None),
                                                                List(elts=[], ctx=Load()),
                                                                Constant(value='id', kind=None),
                                                                Constant(value='base_import.tests.models.m2o', kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='id', kind=None),
                                                                Constant(value='name', kind=None),
                                                                Constant(value='string', kind=None),
                                                                Constant(value='required', kind=None),
                                                                Constant(value='fields', kind=None),
                                                                Constant(value='type', kind=None),
                                                                Constant(value='model_name', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='.id', kind=None),
                                                                Constant(value='Database ID', kind=None),
                                                                Constant(value=False, kind=None),
                                                                List(elts=[], ctx=Load()),
                                                                Constant(value='id', kind=None),
                                                                Constant(value='base_import.tests.models.m2o', kind=None),
                                                            ],
                                                        ),
                                                    ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_m2o_required',
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
                            value=Constant(value=' If an m2o field is required, its three sub-fields are\n        required as well (the client has to handle that: requiredness\n        is id-based)\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='m2o.required', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='make_field', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='field_type',
                                                value=Constant(value='many2one', kind=None),
                                            ),
                                            keyword(
                                                arg='required',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='comodel_name',
                                                value=Constant(value='base_import.tests.models.m2o.required.related', kind=None),
                                            ),
                                            keyword(
                                                arg='model_name',
                                                value=Constant(value='base_import.tests.models.m2o.required', kind=None),
                                            ),
                                            keyword(
                                                arg='fields',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='id', kind=None),
                                                                Constant(value='name', kind=None),
                                                                Constant(value='string', kind=None),
                                                                Constant(value='required', kind=None),
                                                                Constant(value='fields', kind=None),
                                                                Constant(value='type', kind=None),
                                                                Constant(value='model_name', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='id', kind=None),
                                                                Constant(value='External ID', kind=None),
                                                                Constant(value=True, kind=None),
                                                                List(elts=[], ctx=Load()),
                                                                Constant(value='id', kind=None),
                                                                Constant(value='base_import.tests.models.m2o.required', kind=None),
                                                            ],
                                                        ),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='id', kind=None),
                                                                Constant(value='name', kind=None),
                                                                Constant(value='string', kind=None),
                                                                Constant(value='required', kind=None),
                                                                Constant(value='fields', kind=None),
                                                                Constant(value='type', kind=None),
                                                                Constant(value='model_name', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='.id', kind=None),
                                                                Constant(value='Database ID', kind=None),
                                                                Constant(value=True, kind=None),
                                                                List(elts=[], ctx=Load()),
                                                                Constant(value='id', kind=None),
                                                                Constant(value='base_import.tests.models.m2o.required', kind=None),
                                                            ],
                                                        ),
                                                    ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestO2M',
            bases=[Name(id='BaseImportCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='get_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_fields_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='base_import.tests.models.', kind=None),
                                        op=Add(),
                                        right=Name(id='field', ctx=Load()),
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
                    name='test_shallow',
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
                                    attr='assertEqualFields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='o2m', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='ID_FIELD', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='Name', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='char', kind=None),
                                                    Constant(value='base_import.tests.models.o2m', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='comodel_name', kind=None),
                                                    Constant(value='fields', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='Value', kind=None),
                                                    Constant(value='base_import.tests.models.o2m', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='one2many', kind=None),
                                                    Constant(value='base_import.tests.models.o2m.child', kind=None),
                                                    List(
                                                        elts=[
                                                            Name(id='ID_FIELD', ctx=Load()),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='model_name', kind=None),
                                                                    Constant(value='string', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='comodel_name', kind=None),
                                                                    Constant(value='required', kind=None),
                                                                    Constant(value='fields', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='parent_id', kind=None),
                                                                    Constant(value='parent_id', kind=None),
                                                                    Constant(value='base_import.tests.models.o2m.child', kind=None),
                                                                    Constant(value='Parent', kind=None),
                                                                    Constant(value='many2one', kind=None),
                                                                    Constant(value='base_import.tests.models.o2m', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='id', kind=None),
                                                                                    Constant(value='name', kind=None),
                                                                                    Constant(value='model_name', kind=None),
                                                                                    Constant(value='string', kind=None),
                                                                                    Constant(value='required', kind=None),
                                                                                    Constant(value='fields', kind=None),
                                                                                    Constant(value='type', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Constant(value='parent_id', kind=None),
                                                                                    Constant(value='id', kind=None),
                                                                                    Constant(value='base_import.tests.models.o2m.child', kind=None),
                                                                                    Constant(value='External ID', kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    List(elts=[], ctx=Load()),
                                                                                    Constant(value='id', kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='id', kind=None),
                                                                                    Constant(value='name', kind=None),
                                                                                    Constant(value='model_name', kind=None),
                                                                                    Constant(value='string', kind=None),
                                                                                    Constant(value='required', kind=None),
                                                                                    Constant(value='fields', kind=None),
                                                                                    Constant(value='type', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Constant(value='parent_id', kind=None),
                                                                                    Constant(value='.id', kind=None),
                                                                                    Constant(value='base_import.tests.models.o2m.child', kind=None),
                                                                                    Constant(value='Database ID', kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    List(elts=[], ctx=Load()),
                                                                                    Constant(value='id', kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='string', kind=None),
                                                                    Constant(value='required', kind=None),
                                                                    Constant(value='fields', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='model_name', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='Value', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    List(elts=[], ctx=Load()),
                                                                    Constant(value='integer', kind=None),
                                                                    Constant(value='base_import.tests.models.o2m.child', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestMatchHeadersSingle',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_match_by_name',
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
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_mapping_suggestion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='f0', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='f0', kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='match', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='field_path', kind=None),
                                            Constant(value='distance', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[Constant(value='f0', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
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
                    name='test_match_by_string',
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
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_mapping_suggestion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='some field', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='bob', kind=None),
                                                    Constant(value='Some Field', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='match', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='field_path', kind=None),
                                            Constant(value='distance', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[Constant(value='bob', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
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
                    name='test_nomatch',
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
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_mapping_suggestion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='should not be', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='bob', kind=None),
                                                    Constant(value='wheee', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='match', ctx=Load()),
                                    Dict(keys=[], values=[]),
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
                    name='test_close_match',
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
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_mapping_suggestion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='bobe', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='bob', kind=None),
                                                    Constant(value='char', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='char', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='match', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='field_path', kind=None),
                                            Constant(value='distance', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[Constant(value='bob', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value=0.1428571428571429, kind=None),
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
                    name='test_distant_match',
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
                            targets=[Name(id='Import', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='base_import.import', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='header', ctx=Store()),
                                        Name(id='field_string', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value='same Folding', kind=None),
                                    Constant(value='Some Field', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Import', ctx=Load()),
                                    attr='_get_mapping_suggestion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='header', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='bob', kind=None),
                                                    Name(id='field_string', ctx=Load()),
                                                    Constant(value='char', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='char', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='string_field_dist', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Import', ctx=Load()),
                                    attr='_get_distance',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='header', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='field_string', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='string_field_dist', ctx=Load()),
                                    Constant(value=0.36363636363636365, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='match', ctx=Load()),
                                    Dict(keys=[], values=[]),
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
                    name='test_recursive_match',
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
                            targets=[Name(id='f', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='string', kind=None),
                                    Constant(value='fields', kind=None),
                                ],
                                values=[
                                    Constant(value='f0', kind=None),
                                    Constant(value='My Field', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='fields', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='f0', kind=None),
                                                    Constant(value='Sub field 0', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='fields', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='f1', kind=None),
                                                    Constant(value='Sub field 2', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_mapping_suggestion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='f0/f1', kind=None),
                                    List(
                                        elts=[Name(id='f', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='match', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='field_path', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='f', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='f', ctx=Load()),
                                                                slice=Constant(value='fields', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='name', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recursive_nomatch',
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
                            value=Constant(value=' Match first level, fail to match second level\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='string', kind=None),
                                    Constant(value='fields', kind=None),
                                ],
                                values=[
                                    Constant(value='f0', kind=None),
                                    Constant(value='My Field', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='fields', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='f0', kind=None),
                                                    Constant(value='Sub field 0', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='fields', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='f1', kind=None),
                                                    Constant(value='Sub field 2', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_mapping_suggestion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='f0/f2', kind=None),
                                    List(
                                        elts=[Name(id='f', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='match', ctx=Load()),
                                    Dict(keys=[], values=[]),
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
        ClassDef(
            name='TestMatchHeadersMultiple',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_noheaders',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base_import.import', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_mapping_suggestions',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(elts=[], ctx=Load()),
                                            Dict(keys=[], values=[]),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
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
                    name='test_nomatch',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base_import.import', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_mapping_suggestions',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                    Constant(value='qux', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value='foo', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value='bar', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=2, kind=None),
                                                            Constant(value='baz', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=3, kind=None),
                                                            Constant(value='qux', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[Constant(value='int', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='char', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='text', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='many2one', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='bar', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value='qux', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
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
                    name='test_mixed',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base_import.import', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_mapping_suggestions',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='foo bar baz qux/corge', kind=None),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Dict(
                                                keys=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value='foo', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value='bar', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=2, kind=None),
                                                            Constant(value='baz', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=3, kind=None),
                                                            Constant(value='qux/corge', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[Constant(value='int', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='char', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='text', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='text', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='string', kind=None),
                                                            Constant(value='type', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='bar', kind=None),
                                                            Constant(value='Bar', kind=None),
                                                            Constant(value='char', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='string', kind=None),
                                                            Constant(value='type', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='bob', kind=None),
                                                            Constant(value='Baz', kind=None),
                                                            Constant(value='text', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='string', kind=None),
                                                            Constant(value='type', kind=None),
                                                            Constant(value='fields', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='qux', kind=None),
                                                            Constant(value='Qux', kind=None),
                                                            Constant(value='many2one', kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='type', kind=None),
                                                                            Constant(value='fields', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='corge', kind=None),
                                                                            Constant(value='text', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='bar', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value='qux/corge', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='field_path', kind=None),
                                                    Constant(value='distance', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[Constant(value='bar', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='field_path', kind=None),
                                                    Constant(value='distance', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[Constant(value='bob', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='field_path', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Constant(value='qux', kind=None),
                                                            Constant(value='corge', kind=None),
                                                        ],
                                                        ctx=Load(),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestColumnMapping',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_column_mapping',
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
                            targets=[Name(id='import_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                            Constant(value='file_name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='Name,Some Value,value\nchhagan,10,1\nmagan,20,2\n', kind='u'),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='text/csv', kind=None),
                                            Constant(value='data.csv', kind=None),
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
                                    value=Name(id='import_record', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='somevalue', kind=None),
                                            Constant(value='othervalue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='Name', kind=None),
                                            Constant(value='Some Value', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.mapping', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='column_name', kind=None),
                                            Constant(value='field_name', kind=None),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='f', ctx=Load()),
                                            slice=Constant(value='column_name', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='f', ctx=Store()),
                                                iter=Name(id='fields', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='Name', kind=None),
                                            Constant(value='Some Value', kind=None),
                                            Constant(value='value', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='f', ctx=Load()),
                                            slice=Constant(value='field_name', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='f', ctx=Store()),
                                                iter=Name(id='fields', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='somevalue', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='othervalue', kind=None),
                                        ],
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
                    name='test_fuzzy_match_distance',
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
                            targets=[Name(id='values_to_test', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='opportunities', kind=None),
                                            Constant(value='opportinuties', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='opportunities', kind=None),
                                            Constant(value='opportunate', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='opportunities', kind=None),
                                            Constant(value='operable', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='opportunities', kind=None),
                                            Constant(value='purchasing', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lead_id', kind=None),
                                            Constant(value='laed_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lead_id', kind=None),
                                            Constant(value='leen_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lead_id', kind=None),
                                            Constant(value='let_id_be', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lead_id', kind=None),
                                            Constant(value='not related', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Import', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='base_import.import', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='max_distance', ctx=Store())],
                            value=Constant(value=0.2, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='value', ctx=Store()),
                            iter=Name(id='values_to_test', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='distance', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Import', ctx=Load()),
                                            attr='_get_distance',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='value', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='value', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model_fields_info', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='type', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='value', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='value', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='char', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base_import.import', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_mapping_suggestion',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='value', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='model_fields_info', ctx=Load()),
                                            List(
                                                elts=[Constant(value='char', kind=None)],
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[Name(id='match', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Name(id='distance', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Name(id='max_distance', ctx=Load())],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestPreview',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='make_import',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                            Constant(value='file_name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='res.users', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='로그인,언어\nbob,1\n', kind='u'),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='euc_kr', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='text/csv', kind=None),
                                            Constant(value='kr_data.csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='import_wizard', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_encoding',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='make_import',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Constant(value='error', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='result', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.base_import.models.base_import', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_csv_errors',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='make_import',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                        ],
                                        values=[
                                            Constant(value='foo', kind=None),
                                            Constant(value=',', kind=None),
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Constant(value='error', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='result', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value='bob', kind=None),
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Constant(value='error', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='result', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.base_import.models.base_import', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_csv_success',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value=b'name,Some Value,Counter\nfoo,,\nbar,,4\nqux,5,6\n', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='matches', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value=0, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[Constant(value='name', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='somevalue', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='Some Value', kind=None),
                                            Constant(value='Counter', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Name(id='ID_FIELD', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='Name', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='char', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='Some Value', kind=None),
                                                    Constant(value=True, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='Other Variable', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='qux', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='5', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='4', kind=None),
                                                    Constant(value='6', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_xls_success',
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
                            targets=[Name(id='xls_file_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Constant(value='base_import', kind=None),
                                    Constant(value='tests', kind=None),
                                    Constant(value='test.xls', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='file_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='xls_file_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Name(id='file_content', ctx=Load()),
                                            Constant(value='application/vnd.ms-excel', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='has_headers', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='matches', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value=0, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[Constant(value='name', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='somevalue', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='Some Value', kind=None),
                                            Constant(value='Counter', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Name(id='ID_FIELD', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='Name', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='char', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='Some Value', kind=None),
                                                    Constant(value=True, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='Other Variable', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='qux', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='3', kind=None),
                                                    Constant(value='5', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='2', kind=None),
                                                    Constant(value='4', kind=None),
                                                    Constant(value='6', kind=None),
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='unittest', ctx=Load()),
                                attr='skipUnless',
                                ctx=Load(),
                            ),
                            args=[
                                Call(
                                    func=Name(id='can_import', ctx=Load()),
                                    args=[Constant(value='xlrd', kind=None)],
                                    keywords=[],
                                ),
                                Constant(value='XLRD module not available', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_xlsx_success',
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
                            targets=[Name(id='xlsx_file_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Constant(value='base_import', kind=None),
                                    Constant(value='tests', kind=None),
                                    Constant(value='test.xlsx', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='file_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='xlsx_file_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Name(id='file_content', ctx=Load()),
                                            Constant(value='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='has_headers', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='matches', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value=0, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[Constant(value='name', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='somevalue', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='Some Value', kind=None),
                                            Constant(value='Counter', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Name(id='ID_FIELD', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='Name', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='char', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='Some Value', kind=None),
                                                    Constant(value=True, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='Other Variable', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='qux', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='3', kind=None),
                                                    Constant(value='5', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='2', kind=None),
                                                    Constant(value='4', kind=None),
                                                    Constant(value='6', kind=None),
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='unittest', ctx=Load()),
                                attr='skipUnless',
                                ctx=Load(),
                            ),
                            args=[
                                Call(
                                    func=Name(id='can_import', ctx=Load()),
                                    args=[Constant(value='xlrd.xlsx', kind=None)],
                                    keywords=[],
                                ),
                                Constant(value='XLRD/XLSX not available', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_ods_success',
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
                            targets=[Name(id='ods_file_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Constant(value='base_import', kind=None),
                                    Constant(value='tests', kind=None),
                                    Constant(value='test.ods', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='file_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='ods_file_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Name(id='file_content', ctx=Load()),
                                            Constant(value='application/vnd.oasis.opendocument.spreadsheet', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='has_headers', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='matches', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value=0, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[Constant(value='name', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='somevalue', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='Some Value', kind=None),
                                            Constant(value='Counter', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Name(id='ID_FIELD', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='Name', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='char', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='somevalue', kind=None),
                                                    Constant(value='Some Value', kind=None),
                                                    Constant(value=True, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='string', kind=None),
                                                    Constant(value='required', kind=None),
                                                    Constant(value='fields', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='model_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='othervalue', kind=None),
                                                    Constant(value='Other Variable', kind=None),
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='base_import.tests.models.preview', kind=None),
                                                ],
                                            ),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='preview', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='foo', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value='2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='unittest', ctx=Load()),
                                attr='skipUnless',
                                ctx=Load(),
                            ),
                            args=[
                                Call(
                                    func=Name(id='can_import', ctx=Load()),
                                    args=[Constant(value='odf', kind=None)],
                                    keywords=[],
                                ),
                                Constant(value='ODFPY not available', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_convert_import_data',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Tests conversion of base_import.import input into data which\n    can be fed to Model.load\n    ', kind=None),
                ),
                FunctionDef(
                    name='test_all',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value=b'name,Some Value,Counter\nfoo,1,2\nbar,3,4\nqux,5,6\n', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='data', ctx=Store()),
                                        Name(id='fields', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_convert_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='somevalue', kind=None),
                                            Constant(value='othervalue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fields', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='somevalue', kind=None),
                                            Constant(value='othervalue', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='1', kind=None),
                                                    Constant(value='2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='3', kind=None),
                                                    Constant(value='4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='qux', kind=None),
                                                    Constant(value='5', kind=None),
                                                    Constant(value='6', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_date_fields',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='res.partner', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='name,date,create_date\n"foo","2013年07月18日","2016-10-12 06:06"\n', kind='u'),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='create_date', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='date_format', kind=None),
                                            Constant(value='datetime_format', kind=None),
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='%Y年%m月%d日', kind=None),
                                            Constant(value='%Y-%m-%d %H:%M', kind=None),
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                    name='test_parse_relational_fields',
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
                            value=Constant(value=' Ensure that relational fields float and date are correctly\n        parsed during the import call.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='res.partner', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='name,parent_id/id,parent_id/date,parent_id/credit_limit\n"foo","__export__.res_partner_1","2017年10月12日","5,69"\n', kind='u'),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='options', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='date_format', kind=None),
                                    Constant(value='quoting', kind=None),
                                    Constant(value='separator', kind=None),
                                    Constant(value='float_decimal_separator', kind=None),
                                    Constant(value='float_thousand_separator', kind=None),
                                    Constant(value='has_headers', kind=None),
                                ],
                                values=[
                                    Constant(value='%Y年%m月%d日', kind=None),
                                    Constant(value='"', kind=None),
                                    Constant(value=',', kind=None),
                                    Constant(value=',', kind=None),
                                    Constant(value='.', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='data', ctx=Store()),
                                        Name(id='import_fields', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_convert_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='parent_id/.id', kind=None),
                                            Constant(value='parent_id/date', kind=None),
                                            Constant(value='parent_id/credit_limit', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_parse_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    Name(id='import_fields', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=5.69, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=2, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='2017-10-12', kind=None),
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
                    name='test_parse_scientific_notation',
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
                            value=Constant(value=' Ensure that scientific notation is correctly converted to decimal ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='base_import.import', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_options', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_data', ctx=Store())],
                            value=List(
                                elts=[
                                    List(
                                        elts=[Constant(value='1E+05', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='1.20E-05', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='1,9e5', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='9,5e-5', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=List(
                                elts=[
                                    List(
                                        elts=[Constant(value='100000.000000', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='0.000012', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='190000.000000', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='0.000095', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_parse_float_from_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_data', ctx=Load()),
                                    Constant(value=0, kind=None),
                                    Constant(value='test-name', kind=None),
                                    Name(id='test_options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_data', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_filtered',
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
                            value=Constant(value=' If ``False`` is provided as field mapping for a column,\n        that column should be removed from importable data\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value=b'name,Some Value,Counter\nfoo,1,2\nbar,3,4\nqux,5,6\n', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='data', ctx=Store()),
                                        Name(id='fields', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_convert_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='othervalue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fields', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='othervalue', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='qux', kind=None),
                                                    Constant(value='6', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_norow',
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
                            value=Constant(value=' If a row is composed only of empty values (due to having\n        filtered out non-empty values from it), it should be removed\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value=b'name,Some Value,Counter\nfoo,1,2\n,3,\n,5,6\n', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='data', ctx=Store()),
                                        Name(id='fields', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_convert_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='othervalue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fields', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='othervalue', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='6', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty_rows',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value=b'name,Some Value\nfoo,1\n\nbar,2\n     \n\t \n', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='data', ctx=Store()),
                                        Name(id='fields', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_convert_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='somevalue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fields', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='somevalue', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='2', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_nofield',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value=b'name,Some Value,Counter\nfoo,1,2\n', kind=None),
                                            Constant(value='text/csv', kind=None),
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
                                    attr='assertRaises',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ImportValidationError', ctx=Load()),
                                    Attribute(
                                        value=Name(id='import_wizard', ctx=Load()),
                                        attr='_convert_import_data',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                    name='test_falsefields',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value=b'name,Some Value,Counter\nfoo,1,2\n', kind=None),
                                            Constant(value='text/csv', kind=None),
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
                                    attr='assertRaises',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ImportValidationError', ctx=Load()),
                                    Attribute(
                                        value=Name(id='import_wizard', ctx=Load()),
                                        attr='_convert_import_data',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                    name='test_newline_import',
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
                            value=Constant(value='\n        Ensure importing keep newlines\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='output', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='output', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='quoting',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data_row', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='\tfoo\n\tbar', kind='u'),
                                    Constant(value=' "hello" \n\n \'world\' ', kind='u'),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind='u'),
                                            Constant(value='Some Value', kind='u'),
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
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data_row', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='output', ctx=Load()),
                                                    attr='getvalue',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='data', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='_convert_import_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='somevalue', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    List(
                                        elts=[Name(id='data_row', ctx=Load())],
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
                    name='test_set_empty_value_import',
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
                            targets=[Name(id='partners_before', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='res.partner', kind=None),
                                            Constant(value='foo,US,person\n\nfoo1,Invalid Country,person\n\nfoo2,US,persons\n', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='company_type', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='import_set_empty_fields', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='country_id', kind=None),
                                                    Constant(value='company_type', kind=None),
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
                            targets=[Name(id='partners_now', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Name(id='partners_before', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    BinOp(
                                        left=Constant(value='should have imported the first 3 records in full, got %s', kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Constant(value='ids', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='partners_now', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='foo', kind=None),
                                    Constant(value="New partner's name should be foo", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Name(id='partners_now', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
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
                                            args=[Constant(value='base.us', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value="Foo partner's country should be US", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='partners_now', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='company_type',
                                        ctx=Load(),
                                    ),
                                    Constant(value='person', kind=None),
                                    Constant(value="Foo partner's country should be person", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Name(id='partners_now', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value="foo1 partner's country should be False", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='partners_now', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='company_type',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value="foo2 partner's country should be False", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                    name='test_skip_record_import',
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
                            targets=[Name(id='partners_before', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='res.partner', kind=None),
                                            Constant(value='foo,US,0,person\n\nfoo1,Invalid Country,0,person\n\nfoo2,US,False Value,person\n\nfoo3,US,0,persons\n', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='is_company', kind=None),
                                            Constant(value='company_type', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='import_skip_records', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='country_id', kind=None),
                                                    Constant(value='is_company', kind=None),
                                                    Constant(value='company_type', kind=None),
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
                            targets=[Name(id='partners_now', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Name(id='partners_before', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    BinOp(
                                        left=Constant(value='should have imported the first record in full, got %s', kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Constant(value='ids', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='partners_now', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='foo', kind=None),
                                    Constant(value="New partner's name should be foo", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
        ClassDef(
            name='TestBatching',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_makefile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rows', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='quoting',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='counter', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Name(id='rows', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='n_%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='i', ctx=Load()),
                                                    ),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='i', ctx=Load())],
                                                        keywords=[],
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
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='getvalue',
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
                    name='test_recognize_batched',
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
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.preview', kind=None),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='file',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_makefile',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                            Constant(value='limit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=100, kind=None),
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='batch', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quoting', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='has_headers', kind=None),
                                            Constant(value='limit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='"', kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=5, kind=None),
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='error', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='batch', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
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
                    name='test_limit_on_lines',
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
                            value=Constant(value=' The limit option should be a limit on the number of *lines*\n        imported at at time, not the number of *records*. This is relevant\n        when it comes to embedded o2m.\n\n        A big question is whether we want to round up or down (if the limit\n        brings us inside a record). Rounding up (aka finishing up the record\n        we\'re currently parsing) seems like a better idea:\n\n        * if the first record has so many sub-lines it hits the limit we still\n          want to import it (it\'s probably extremely rare but it can happen)\n        * if we have one line per record, we probably want to import <limit>\n          records not <limit-1>, but if we stop in the middle of the "current\n          record" we\'d always ignore the last record (I think)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='f', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='quoting',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='record_%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='record', ctx=Load()),
                                                    ),
                                                    Constant(value='0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='row', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=1, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='writer', ctx=Load()),
                                                    attr='writerow',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='row', ctx=Load())],
                                                                keywords=[],
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file_type', kind=None),
                                            Constant(value='file_name', kind=None),
                                            Constant(value='file', kind=None),
                                        ],
                                        values=[
                                            Constant(value='base_import.tests.models.o2m', kind=None),
                                            Constant(value='text/csv', kind=None),
                                            Constant(value='things.csv', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='getvalue',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='opts', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='quoting', kind=None),
                                    Constant(value='separator', kind=None),
                                    Constant(value='has_headers', kind=None),
                                ],
                                values=[
                                    Constant(value='"', kind=None),
                                    Constant(value=',', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='preview', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='parse_preview',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='limit', kind=None),
                                        ],
                                        values=[
                                            Name(id='opts', ctx=Load()),
                                            Constant(value=15, kind=None),
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='preview', ctx=Load()),
                                        slice=Constant(value='batch', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='limit', kind=None),
                                        ],
                                        values=[
                                            Name(id='opts', ctx=Load()),
                                            Constant(value=5, kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    BinOp(
                                        left=Constant(value='should have imported the first record in full, got %s', kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Constant(value='ids', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='nextrow', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=10, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='limit', kind=None),
                                        ],
                                        values=[
                                            Name(id='opts', ctx=Load()),
                                            Constant(value=15, kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    BinOp(
                                        left=Constant(value='should have importe the first two records, got %s', kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Constant(value='ids', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='nextrow', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=20, kind=None),
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
                    name='test_batches',
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
                            targets=[Name(id='partners_before', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='opts', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='has_headers', kind=None),
                                    Constant(value='separator', kind=None),
                                    Constant(value='quoting', kind=None),
                                ],
                                values=[
                                    Constant(value=True, kind=None),
                                    Constant(value=',', kind=None),
                                    Constant(value='"', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file_type', kind=None),
                                            Constant(value='file_name', kind=None),
                                            Constant(value='file', kind=None),
                                        ],
                                        values=[
                                            Constant(value='res.partner', kind=None),
                                            Constant(value='text/csv', kind=None),
                                            Constant(value='clients.csv', kind=None),
                                            Constant(value=b'name,email\na,a@example.com\nb,b@example.com\n,\nc,c@example.com\nd,d@example.com\ne,e@example.com\nf,f@example.com\ng,g@example.com\n', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='limit', kind=None),
                                        ],
                                        values=[
                                            Name(id='opts', ctx=Load()),
                                            Constant(value=1, kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='nextrow', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='partners_1', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Name(id='partners_before', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='partners_1', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='a', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='limit', kind=None),
                                            Constant(value='skip', kind=None),
                                        ],
                                        values=[
                                            Name(id='opts', ctx=Load()),
                                            Constant(value=2, kind=None),
                                            Constant(value=1, kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='nextrow', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='partners_2', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=BinOp(
                                    left=Name(id='partners_before', ctx=Load()),
                                    op=BitOr(),
                                    right=Name(id='partners_1', ctx=Load()),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='partners_2', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='b', kind=None),
                                            Constant(value='c', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='limit', kind=None),
                                            Constant(value='skip', kind=None),
                                        ],
                                        values=[
                                            Name(id='opts', ctx=Load()),
                                            Constant(value=10, kind=None),
                                            Constant(value=3, kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='results', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='nextrow', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='partners_3', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=BinOp(
                                    left=BinOp(
                                        left=Name(id='partners_before', ctx=Load()),
                                        op=BitOr(),
                                        right=Name(id='partners_1', ctx=Load()),
                                    ),
                                    op=BitOr(),
                                    right=Name(id='partners_2', ctx=Load()),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='partners_3', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='d', kind=None),
                                            Constant(value='e', kind=None),
                                            Constant(value='f', kind=None),
                                            Constant(value='g', kind=None),
                                        ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_failures',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_big_attachments',
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
                            value=Constant(value="\n        Ensure big fields (e.g. b64-encoded image data) can be imported and\n        we're not hitting limits of the default CSV parser config\n        ", kind=None),
                        ),
                        ImportFrom(
                            module='PIL',
                            names=[alias(name='Image', asname=None)],
                            level=0,
                        ),
                        Assign(
                            targets=[Name(id='im', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGB', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=1920, kind=None),
                                            Constant(value=1080, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fout', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fout', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dialect',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerows',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='name', kind='u'),
                                                    Constant(value='db_datas', kind='u'),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='foo', kind='u'),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='base64', ctx=Load()),
                                                                    attr='b64encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='im', ctx=Load()),
                                                                            attr='tobytes',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='ascii', kind=None)],
                                                        keywords=[],
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
                        ),
                        Assign(
                            targets=[Name(id='import_wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.import', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='file', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='ir.attachment', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='fout', ctx=Load()),
                                                    attr='getvalue',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='text/csv', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_wizard', ctx=Load()),
                                    attr='execute_import',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='db_datas', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='has_headers', kind=None),
                                            Constant(value='separator', kind=None),
                                            Constant(value='quoting', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value=',', kind=None),
                                            Constant(value='"', kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='results should be empty on successful import', kind=None),
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
    ],
    type_ignores=[],
)
