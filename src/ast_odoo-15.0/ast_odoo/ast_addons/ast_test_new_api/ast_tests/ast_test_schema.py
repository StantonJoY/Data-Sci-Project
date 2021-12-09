Module(
    body=[
        ImportFrom(
            module='odoo.models',
            names=[alias(name='MetaModel', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_model',
            names=[
                alias(name='model_xmlid', asname=None),
                alias(name='field_xmlid', asname=None),
                alias(name='selection_xmlid', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='get_model_name',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cls', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Attribute(
                        value=Name(id='cls', ctx=Load()),
                        attr='_name',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='name', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='name', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_inherit',
                                            ctx=Load(),
                                        ),
                                        Name(id='list', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_inherit',
                                    ctx=Load(),
                                ),
                                orelse=List(
                                    elts=[
                                        Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_inherit',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assert(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='name', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    msg=None,
                ),
                Return(
                    value=Name(id='name', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='TestReflection',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Test the reflection into 'ir.model', 'ir.model.fields', etc. ", kind=None),
                ),
                FunctionDef(
                    name='assertModelXID',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check the XML id of the given 'ir.model' record. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Call(
                                func=Name(id='model_xmlid', ctx=Load()),
                                args=[
                                    Constant(value='test_new_api', kind=None),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='model',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='xid', ctx=Load())],
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
                    name='assertFieldXID',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check the XML id of the given 'ir.model.fields' record. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Call(
                                func=Name(id='field_xmlid', ctx=Load()),
                                args=[
                                    Constant(value='test_new_api', kind=None),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='model',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='xid', ctx=Load())],
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
                    name='assertSelectionXID',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check the XML id of the given 'ir.model.fields.selection' record. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Call(
                                func=Name(id='selection_xmlid', ctx=Load()),
                                args=[
                                    Constant(value='test_new_api', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='field_id',
                                            ctx=Load(),
                                        ),
                                        attr='model',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='field_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='value',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='xid', ctx=Load())],
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
                    name='test_models_fields',
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
                            value=Constant(value=' check that all models and fields are reflected as expected. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model_names', ctx=Store())],
                            value=SetComp(
                                elt=Call(
                                    func=Name(id='get_model_name', ctx=Load()),
                                    args=[Name(id='cls', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='cls', ctx=Store()),
                                        iter=Subscript(
                                            value=Attribute(
                                                value=Name(id='MetaModel', ctx=Load()),
                                                attr='module_to_models',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='test_new_api', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ir_models', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
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
                                                    Constant(value='in', kind=None),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='model_names', ctx=Load())],
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
                                        args=[Name(id='ir_models', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='model_names', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='ir_model', ctx=Store()),
                            iter=Name(id='ir_models', ctx=Load()),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='subTest',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='model',
                                                        value=Attribute(
                                                            value=Name(id='ir_model', ctx=Load()),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='model', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='ir_model', ctx=Load()),
                                                    attr='model',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertModelXID',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='ir_model', ctx=Load())],
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
                                                        value=Name(id='ir_model', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='model', ctx=Load()),
                                                                attr='_description',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
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
                                                    Attribute(
                                                        value=Name(id='ir_model', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Name(id='model', ctx=Load()),
                                                            attr='_custom',
                                                            ctx=Load(),
                                                        ),
                                                        body=Constant(value='manual', kind=None),
                                                        orelse=Constant(value='base', kind=None),
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
                                                        value=Name(id='ir_model', ctx=Load()),
                                                        attr='transient',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='bool', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='model', ctx=Load()),
                                                                attr='_transient',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                    attr='assertItemsEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='ir_model', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='field_id.name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='model', ctx=Load()),
                                                                attr='_fields',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        For(
                                            target=Name(id='ir_field', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='ir_model', ctx=Load()),
                                                attr='field_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='subTest',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='field',
                                                                        value=Attribute(
                                                                            value=Name(id='ir_field', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            optional_vars=None,
                                                        ),
                                                    ],
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='field', ctx=Store())],
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='model', ctx=Load()),
                                                                    attr='_fields',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Attribute(
                                                                    value=Name(id='ir_field', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertFieldXID',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='ir_field', ctx=Load())],
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
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='model',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='model_name',
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='field_description',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='string',
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='help',
                                                                        ctx=Load(),
                                                                    ),
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='help',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='ttype',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='type',
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    IfExp(
                                                                        test=Attribute(
                                                                            value=Name(id='field', ctx=Load()),
                                                                            attr='manual',
                                                                            ctx=Load(),
                                                                        ),
                                                                        body=Constant(value='manual', kind=None),
                                                                        orelse=Constant(value='base', kind=None),
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
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='index',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='index',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='store',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='store',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='copied',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='copy',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='related',
                                                                        ctx=Load(),
                                                                    ),
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='related',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='readonly',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='readonly',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='required',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='required',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='selectable',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='search',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='store',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
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
                                                                    Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='translate',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='translate',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='relational',
                                                                ctx=Load(),
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
                                                                            Attribute(
                                                                                value=Name(id='ir_field', ctx=Load()),
                                                                                attr='relation',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='comodel_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='field', ctx=Load()),
                                                                            attr='type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='one2many', kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='store',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                                                            Attribute(
                                                                                value=Name(id='ir_field', ctx=Load()),
                                                                                attr='relation_field',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='inverse_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='field', ctx=Load()),
                                                                            attr='type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='many2many', kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='store',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                                                            Attribute(
                                                                                value=Name(id='ir_field', ctx=Load()),
                                                                                attr='relation_table',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='relation',
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
                                                                            Attribute(
                                                                                value=Name(id='ir_field', ctx=Load()),
                                                                                attr='column1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='column1',
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
                                                                            Attribute(
                                                                                value=Name(id='ir_field', ctx=Load()),
                                                                                attr='column2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='column2',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='relation', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='ir.model.relation', kind=None),
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
                                                                                            Constant(value='name', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                attr='relation',
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
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='assertTrue',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='relation', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='assertIn',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='relation', ctx=Load()),
                                                                                    attr='model',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='model',
                                                                                ctx=Load(),
                                                                            ),
                                                                            List(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='model_name',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='comodel_name',
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
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='field', ctx=Load()),
                                                                    attr='type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='selection', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='selection', ctx=Store())],
                                                                    value=ListComp(
                                                                        elt=Tuple(
                                                                            elts=[
                                                                                Attribute(
                                                                                    value=Name(id='sel', ctx=Load()),
                                                                                    attr='value',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='sel', ctx=Load()),
                                                                                    attr='name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='sel', ctx=Store()),
                                                                                iter=Attribute(
                                                                                    value=Name(id='ir_field', ctx=Load()),
                                                                                    attr='selection_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Call(
                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='field', ctx=Load()),
                                                                                attr='selection',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='list', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
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
                                                                                    Name(id='selection', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='field', ctx=Load()),
                                                                                        attr='selection',
                                                                                        ctx=Load(),
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
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='assertEqual',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Name(id='selection', ctx=Load()),
                                                                                    List(elts=[], ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                For(
                                                                    target=Name(id='sel', ctx=Store()),
                                                                    iter=Attribute(
                                                                        value=Name(id='ir_field', ctx=Load()),
                                                                        attr='selection_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='assertSelectionXID',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='sel', ctx=Load())],
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
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='field_description', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='get_description',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='many2many', kind=None),
                                                            Constant(value='one2many', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertFalse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='field_description', ctx=Load()),
                                                                slice=Constant(value='sortable', kind=None),
                                                                ctx=Load(),
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
                                                            Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='store',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='column_type',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertTrue',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='field_description', ctx=Load()),
                                                                        slice=Constant(value='sortable', kind=None),
                                                                        ctx=Load(),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestSchema',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='get_table_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tablename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value=' SELECT table_catalog, table_schema, table_name, table_type,\n                           user_defined_type_catalog, user_defined_type_schema,\n                           user_defined_type_name, is_insertable_into, is_typed\n                    FROM information_schema.tables\n                    WHERE table_name=%s ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    List(
                                        elts=[Name(id='tablename', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='dictfetchone',
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
                    name='get_columns_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tablename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value=' SELECT table_catalog, table_schema, table_name, column_name,\n                           column_default, data_type, is_nullable, is_updatable,\n                           character_maximum_length, numeric_precision,\n                           numeric_precision_radix, numeric_scale,\n                           datetime_precision, udt_catalog, udt_schema, udt_name\n                    FROM information_schema.columns\n                    WHERE table_name=%s ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    List(
                                        elts=[Name(id='tablename', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='row', ctx=Load()),
                                    slice=Constant(value='column_name', kind=None),
                                    ctx=Load(),
                                ),
                                value=Name(id='row', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='row', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dictfetchall',
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
                FunctionDef(
                    name='get_foreign_keys',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tablename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value=' SELECT a.table_name, a.column_name,\n                           b.table_name, b.column_name, c.delete_rule\n                    FROM information_schema.referential_constraints c,\n                         information_schema.key_column_usage a,\n                         information_schema.constraint_column_usage b\n                    WHERE a.constraint_schema=c.constraint_schema\n                      AND a.constraint_name=c.constraint_name\n                      AND b.constraint_schema=c.constraint_schema\n                      AND b.constraint_name=c.constraint_name\n                      AND a.table_name=%s ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    List(
                                        elts=[Name(id='tablename', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
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
                    name='test_00_table',
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
                            value=Constant(value=' check the database schema of a model ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.foo', kind=None),
                                ctx=Load(),
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
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
                                        ctx=Load(),
                                    ),
                                    Constant(value='test_new_api_foo', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='table_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_table_data',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='test_new_api_foo', kind=None)],
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
                                    Name(id='table_data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='is_insertable_into', kind=None),
                                            Constant(value='is_typed', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='table_type', kind=None),
                                            Constant(value='user_defined_type_catalog', kind=None),
                                            Constant(value='user_defined_type_name', kind=None),
                                            Constant(value='user_defined_type_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value='YES', kind='u'),
                                            Constant(value='NO', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_foo', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Constant(value='BASE TABLE', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='test_new_api_foo', kind=None)],
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
                                        func=Name(id='set', ctx=Load()),
                                        args=[Name(id='columns_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Set(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='create_date', kind=None),
                                            Constant(value='create_uid', kind=None),
                                            Constant(value='write_date', kind=None),
                                            Constant(value='write_uid', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='value1', kind=None),
                                            Constant(value='value2', kind=None),
                                            Constant(value='text', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='foreign_keys', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_foreign_keys',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='test_new_api_foo', kind=None)],
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
                                    Name(id='foreign_keys', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='test_new_api_foo', kind=None),
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='res_users', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='SET NULL', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='test_new_api_foo', kind=None),
                                                    Constant(value='write_uid', kind=None),
                                                    Constant(value='res_users', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='SET NULL', kind=None),
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
                    name='test_10_boolean',
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
                            value=Constant(value=' check the database representation of a boolean field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.message', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='important', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='important', kind='u'),
                                            Constant(value='boolean', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_message', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='bool', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_integer',
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
                            value=Constant(value=' check the database representation of an integer field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.category', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='color', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='color', kind='u'),
                                            Constant(value='integer', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=32, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_category', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='int4', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_float',
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
                            value=Constant(value=' check the database representation of a float field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='number', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='number', kind='u'),
                                            Constant(value='numeric', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='numeric', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_monetary',
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
                            value=Constant(value=' check the database representation of a monetary field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='amount', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='amount', kind='u'),
                                            Constant(value='numeric', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='numeric', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_char',
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
                            value=Constant(value=' check the database representation of a char field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.country', kind=None),
                                ctx=Load(),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Name(id='type', ctx=Load()),
                                                args=[Name(id='model', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        attr='required',
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
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Name(id='type', ctx=Load()),
                                                args=[Name(id='model', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='code', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=2, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='code', kind='u'),
                                            Constant(value='character varying', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='res_country', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='varchar', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.message', kind=None),
                                ctx=Load(),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Name(id='type', ctx=Load()),
                                                args=[Name(id='model', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        attr='required',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='name', kind='u'),
                                            Constant(value='character varying', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_message', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='varchar', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.category', kind=None),
                                ctx=Load(),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Call(
                                                func=Name(id='type', ctx=Load()),
                                                args=[Name(id='model', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        attr='required',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='name', kind='u'),
                                            Constant(value='character varying', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='NO', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_category', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='varchar', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_text',
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
                            value=Constant(value=' check the database representation of a text field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.message', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='body', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='body', kind='u'),
                                            Constant(value='text', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_message', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='text', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_html',
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
                            value=Constant(value=' check the database representation of an html field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='comment1', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='comment1', kind='u'),
                                            Constant(value='text', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='text', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_date',
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
                            value=Constant(value=' check the database representation of a date field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='date', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='date', kind='u'),
                                            Constant(value='date', kind='u'),
                                            Constant(value=0, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='date', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_datetime',
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
                            value=Constant(value=' check the database representation of a datetime field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.property', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='value_datetime', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='value_datetime', kind='u'),
                                            Constant(value='timestamp without time zone', kind='u'),
                                            Constant(value=6, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ir_property', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='timestamp', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='create_date', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='create_date', kind='u'),
                                            Constant(value='timestamp without time zone', kind='u'),
                                            Constant(value=6, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='timestamp', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_selection',
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
                            value=Constant(value=' check the database representation of a selection field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='lang', kind='u'),
                                            Constant(value='character varying', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='varchar', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_reference',
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
                            value=Constant(value=' check the database representation of a reference field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='reference', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='reference', kind='u'),
                                            Constant(value='character varying', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='varchar', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
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
                    name='test_10_many2one',
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
                            value=Constant(value=' check the database representation of a many2one field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.mixed', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='columns_data', ctx=Load()),
                                        slice=Constant(value='currency_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='character_maximum_length', kind=None),
                                            Constant(value='column_default', kind=None),
                                            Constant(value='column_name', kind=None),
                                            Constant(value='data_type', kind=None),
                                            Constant(value='datetime_precision', kind=None),
                                            Constant(value='is_nullable', kind=None),
                                            Constant(value='is_updatable', kind=None),
                                            Constant(value='numeric_precision', kind=None),
                                            Constant(value='numeric_precision_radix', kind=None),
                                            Constant(value='numeric_scale', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='udt_catalog', kind=None),
                                            Constant(value='udt_name', kind=None),
                                            Constant(value='udt_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='currency_id', kind='u'),
                                            Constant(value='integer', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value='YES', kind='u'),
                                            Constant(value='YES', kind='u'),
                                            Constant(value=32, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_mixed', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='int4', kind='u'),
                                            Constant(value='pg_catalog', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='foreign_keys', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_foreign_keys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='test_new_api_mixed', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='res_currency', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='SET NULL', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='foreign_keys', ctx=Load()),
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
                    name='test_10_many2many',
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
                            value=Constant(value=' check the database representation of a many2many field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_new_api.discussion', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='type', ctx=Load()),
                                    args=[Name(id='model', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='categories',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='comodel', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='comodel_name',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='relation',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='column1',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='column2',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='_table',
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
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='categories', kind=None),
                                    Name(id='columns_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='table_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_table_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='relation',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='table_data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='is_insertable_into', kind=None),
                                            Constant(value='is_typed', kind=None),
                                            Constant(value='table_catalog', kind=None),
                                            Constant(value='table_name', kind=None),
                                            Constant(value='table_schema', kind=None),
                                            Constant(value='table_type', kind=None),
                                            Constant(value='user_defined_type_catalog', kind=None),
                                            Constant(value='user_defined_type_name', kind=None),
                                            Constant(value='user_defined_type_schema', kind=None),
                                        ],
                                        values=[
                                            Constant(value='YES', kind='u'),
                                            Constant(value='NO', kind='u'),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_new_api_discussion_category', kind='u'),
                                            Constant(value='public', kind='u'),
                                            Constant(value='BASE TABLE', kind='u'),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='columns_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_columns_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='relation',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='columns_data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='field', ctx=Load()),
                                                attr='column1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='field', ctx=Load()),
                                                attr='column2',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='character_maximum_length', kind=None),
                                                    Constant(value='column_default', kind=None),
                                                    Constant(value='column_name', kind=None),
                                                    Constant(value='data_type', kind=None),
                                                    Constant(value='datetime_precision', kind=None),
                                                    Constant(value='is_nullable', kind=None),
                                                    Constant(value='is_updatable', kind=None),
                                                    Constant(value='numeric_precision', kind=None),
                                                    Constant(value='numeric_precision_radix', kind=None),
                                                    Constant(value='numeric_scale', kind=None),
                                                    Constant(value='table_catalog', kind=None),
                                                    Constant(value='table_name', kind=None),
                                                    Constant(value='table_schema', kind=None),
                                                    Constant(value='udt_catalog', kind=None),
                                                    Constant(value='udt_name', kind=None),
                                                    Constant(value='udt_schema', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='discussion', kind='u'),
                                                    Constant(value='integer', kind='u'),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='NO', kind='u'),
                                                    Constant(value='YES', kind='u'),
                                                    Constant(value=32, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='test_new_api_discussion_category', kind='u'),
                                                    Constant(value='public', kind='u'),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='int4', kind='u'),
                                                    Constant(value='pg_catalog', kind='u'),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='character_maximum_length', kind=None),
                                                    Constant(value='column_default', kind=None),
                                                    Constant(value='column_name', kind=None),
                                                    Constant(value='data_type', kind=None),
                                                    Constant(value='datetime_precision', kind=None),
                                                    Constant(value='is_nullable', kind=None),
                                                    Constant(value='is_updatable', kind=None),
                                                    Constant(value='numeric_precision', kind=None),
                                                    Constant(value='numeric_precision_radix', kind=None),
                                                    Constant(value='numeric_scale', kind=None),
                                                    Constant(value='table_catalog', kind=None),
                                                    Constant(value='table_name', kind=None),
                                                    Constant(value='table_schema', kind=None),
                                                    Constant(value='udt_catalog', kind=None),
                                                    Constant(value='udt_name', kind=None),
                                                    Constant(value='udt_schema', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='category', kind='u'),
                                                    Constant(value='integer', kind='u'),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='NO', kind='u'),
                                                    Constant(value='YES', kind='u'),
                                                    Constant(value=32, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='test_new_api_discussion_category', kind='u'),
                                                    Constant(value='public', kind='u'),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='int4', kind='u'),
                                                    Constant(value='pg_catalog', kind='u'),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='foreign_keys', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_foreign_keys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='relation',
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
                                    Name(id='foreign_keys', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='relation',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='column1',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='_table',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='CASCADE', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='relation',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='column2',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='comodel', ctx=Load()),
                                                        attr='_table',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='CASCADE', kind=None),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
