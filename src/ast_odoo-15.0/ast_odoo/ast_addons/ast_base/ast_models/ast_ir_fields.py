Module(
    body=[
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='Command', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='ustr', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='REFERENCING_FIELDS', ctx=Store())],
            value=Set(
                elts=[
                    Constant(value=None, kind=None),
                    Constant(value='id', kind=None),
                    Constant(value='.id', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='only_ref_fields',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='record', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=DictComp(
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
                                        value=Name(id='record', ctx=Load()),
                                        attr='items',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[
                                    Compare(
                                        left=Name(id='k', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='REFERENCING_FIELDS', ctx=Load())],
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
        FunctionDef(
            name='exclude_ref_fields',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='record', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=DictComp(
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
                                        value=Name(id='record', ctx=Load()),
                                        attr='items',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[
                                    Compare(
                                        left=Name(id='k', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='REFERENCING_FIELDS', ctx=Load())],
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
        ClassDef(
            name='ImportWarning',
            bases=[Name(id='Warning', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Used to send warnings upwards the stack during the import process ', kind=None),
                ),
                Pass(),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ConversionNotFound',
            bases=[Name(id='ValueError', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='IrFieldsConverter',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.fields.converter', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Fields Converter', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_format_import_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='error_type', annotation=None, type_comment=None),
                            arg(arg='error_msg', annotation=None, type_comment=None),
                            arg(arg='error_params', annotation=None, type_comment=None),
                            arg(arg='error_args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Tuple(elts=[], ctx=Load()),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='sanitize', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='p', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=IfExp(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='p', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=Call(
                                        func=Attribute(
                                            value=Name(id='p', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='%', kind=None),
                                            Constant(value='%%', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    orelse=Name(id='p', ctx=Load()),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='error_params', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='error_params', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='error_params', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sanitize', ctx=Load()),
                                                args=[Name(id='error_params', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='error_params', ctx=Load()),
                                                    Name(id='dict', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='error_params', ctx=Store())],
                                                    value=DictComp(
                                                        key=Name(id='k', ctx=Load()),
                                                        value=Call(
                                                            func=Name(id='sanitize', ctx=Load()),
                                                            args=[Name(id='v', ctx=Load())],
                                                            keywords=[],
                                                        ),
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
                                                                        value=Name(id='error_params', ctx=Load()),
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
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='error_params', ctx=Load()),
                                                            Name(id='tuple', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='error_params', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='tuple', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Call(
                                                                            func=Name(id='sanitize', ctx=Load()),
                                                                            args=[Name(id='v', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='v', ctx=Store()),
                                                                                iter=Name(id='error_params', ctx=Load()),
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
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='error_type', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='error_msg', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='error_params', ctx=Load()),
                                    ),
                                    Name(id='error_args', ctx=Load()),
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
                    name='_get_import_field_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Rebuild field path for import error attribution to the right field.\n        This method uses the 'parent_fields_hierarchy' context key built during treatment of one2many fields\n        (_str_to_one2many). As the field to import is the last of the chain (child_id/child_id2/field_to_import),\n        we need to retrieve the complete hierarchy in case of error in order to assign the error to the correct\n        column in the import UI.\n\n        :param (str) field: field in which the value will be imported.\n        :param (str or list) value:\n            - str: in most of the case the value we want to import into a field is a string (or a number).\n            - list: when importing into a one2may field, all the records to import are regrouped into a list of dict.\n                E.g.: creating multiple partners: [{None: 'ChildA_1', 'type': 'Private address'}, {None: 'ChildA_2', 'type': 'Private address'}]\n                where 'None' is the name. (because we can find a partner by his name, we don't need to specify the field.)\n\n        The field_path value is computed based on the last field in the chain.\n        for example,\n            - path_field for 'Private address' at childA_1 is ['partner_id', 'type']\n            - path_field for 'childA_1' is ['partner_id']\n\n        So, by retrieving the correct field_path for each value to import, if errors are raised for those fields,\n        we can the link the errors to the correct header-field couple in the import UI.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_path', ctx=Store())],
                            value=List(
                                elts=[Name(id='field', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='parent_fields_hierarchy', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='parent_fields_hierarchy', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='parent_fields_hierarchy', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='field_path', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='parent_fields_hierarchy', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='field_path', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='field_path_value', ctx=Store())],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='field_path_value', ctx=Load()),
                                    Name(id='list', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='key', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Name(id='list', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='field_path_value', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='keys',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='key', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='field_path', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='key', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='field_path_value', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='field_path_value', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='key', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='field_path', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='for_model',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='fromtype', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Name(id='str', ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns a converter object for the model. A converter is a\n        callable taking a record-ish (a dictionary representing an odoo\n        record with values of typetag ``fromtype``) and returning a converted\n        records matching what :meth:`odoo.osv.orm.Model.write` expects.\n\n        :param model: :class:`odoo.osv.orm.Model` for the conversion base\n        :returns: a converter callable\n        :rtype: (record: dict, logger: (field, error) -> None) -> dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converters', ctx=Store())],
                            value=DictComp(
                                key=Name(id='name', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='to_field',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='model', ctx=Load()),
                                        Name(id='field', ctx=Load()),
                                        Name(id='fromtype', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='name', ctx=Store()),
                                                Name(id='field', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='model', ctx=Load()),
                                                    attr='_fields',
                                                    ctx=Load(),
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
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='fn',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='record', annotation=None, type_comment=None),
                                    arg(arg='log', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='converted', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='import_file_context', ctx=Store())],
                                    value=Call(
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
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='import_file', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='field', ctx=Store()),
                                            Name(id='value', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='field', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='REFERENCING_FIELDS', ctx=Load())],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='value', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='converted', ctx=Load()),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='converted', ctx=Load()),
                                                                    slice=Name(id='field', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                                Name(id='ws', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Subscript(
                                                            value=Name(id='converters', ctx=Load()),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='w', ctx=Store()),
                                                    iter=Name(id='ws', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='w', ctx=Load()),
                                                                    Name(id='str', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='w', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='ImportWarning', ctx=Load()),
                                                                        args=[Name(id='w', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='log', ctx=Load()),
                                                                args=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Name(id='w', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='UnicodeEncodeError', ctx=Load()),
                                                            Name(id='UnicodeDecodeError', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name='e',
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='log', ctx=Load()),
                                                                args=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='ValueError', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[Name(id='e', ctx=Load())],
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
                                                ),
                                                ExceptHandler(
                                                    type=Name(id='ValueError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        If(
                                                            test=Name(id='import_file_context', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='error_info', ctx=Store())],
                                                                    value=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='e', ctx=Load()),
                                                                                            attr='args',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Gt()],
                                                                                comparators=[Constant(value=1, kind=None)],
                                                                            ),
                                                                            Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='e', ctx=Load()),
                                                                                    attr='args',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=1, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='error_info', ctx=Load()),
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='error_info', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='field_path', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='error_info', ctx=Load()),
                                                                                    slice=Constant(value='field_path', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_get_import_field_path',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Name(id='field', ctx=Load()),
                                                                                    Name(id='value', ctx=Load()),
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
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='log', ctx=Load()),
                                                                args=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Name(id='e', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='converted', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='fn', ctx=Load()),
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
                    name='to_field',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='fromtype', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Name(id='str', ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Fetches a converter for the provided field object, from the\n        specified type.\n\n        A converter is simply a callable taking a value of type ``fromtype``\n        (or a composite of ``fromtype``, e.g. list or dict) and returning a\n        value acceptable for a write() on the field ``field``.\n\n        By default, tries to get a method on itself with a name matching the\n        pattern ``_$fromtype_to_$field.type`` and returns it.\n\n        Converter callables can either return a value and a list of warnings\n        to their caller or raise ``ValueError``, which will be interpreted as a\n        validation & conversion failure.\n\n        ValueError can have either one or two parameters. The first parameter\n        is mandatory, **must** be a unicode string and will be used as the\n        user-visible message for the error (it should be translatable and\n        translated). It can contain a ``field`` named format placeholder so the\n        caller can inject the field's translated, user-facing name (@string).\n\n        The second parameter is optional and, if provided, must be a mapping.\n        This mapping will be merged into the error dictionary returned to the\n        client.\n\n        If a converter can perform its function but has to make assumptions\n        about the data, it can send a warning to the user through adding an\n        instance of :class:`~.ImportWarning` to the second value\n        it returns. The handling of a warning at the upper levels is the same\n        as ``ValueError`` above.\n\n        :param field: field object to generate a value for\n        :type field: :class:`odoo.fields.Field`\n        :param fromtype: type to convert to something fitting for ``field``\n        :type fromtype: type | str\n        :param context: odoo request context\n        :return: a function (fromtype -> field.write_type), if a converter is found\n        :rtype: Callable | None\n        ", kind=None),
                        ),
                        Assert(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='fromtype', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='type', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='typename', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='fromtype', ctx=Load()),
                                        Name(id='type', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=Attribute(
                                    value=Name(id='fromtype', ctx=Load()),
                                    attr='__name__',
                                    ctx=Load(),
                                ),
                                orelse=Name(id='fromtype', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converter', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='_%s_to_%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='typename', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='converter', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='functools', ctx=Load()),
                                    attr='partial',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='converter', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                    Name(id='field', ctx=Load()),
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
                    name='_str_to_boolean',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
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
                            targets=[Name(id='trues', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='word', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='word', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='itertools', ctx=Load()),
                                                        attr='chain',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Constant(value='1', kind='u'),
                                                                Constant(value='true', kind='u'),
                                                                Constant(value='yes', kind='u'),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_get_translations',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Constant(value='code', kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='true', kind='u'),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_get_translations',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Constant(value='code', kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='yes', kind='u'),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[Name(id='trues', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=True, kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='falses', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='word', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='word', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='itertools', ctx=Load()),
                                                        attr='chain',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Constant(value='', kind='u'),
                                                                Constant(value='0', kind='u'),
                                                                Constant(value='false', kind='u'),
                                                                Constant(value='no', kind='u'),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_get_translations',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Constant(value='code', kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='false', kind='u'),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_get_translations',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Constant(value='code', kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='no', kind='u'),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[Name(id='falses', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
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
                                        args=[
                                            Constant(value='import_skip_records', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value=True, kind=None),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_format_import_error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="Unknown value '%s' for boolean field '%%(field)s'", kind='u')],
                                                        keywords=[],
                                                    ),
                                                    Name(id='value', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='moreinfo', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value="Use '1' for yes and '0' for no", kind='u')],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
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
                    name='_str_to_integer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_format_import_error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="'%s' does not seem to be an integer for field '%%(field)s'", kind='u')],
                                                        keywords=[],
                                                    ),
                                                    Name(id='value', ctx=Load()),
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
                    name='_str_to_float',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='float', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_format_import_error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="'%s' does not seem to be a number for field '%%(field)s'", kind='u')],
                                                        keywords=[],
                                                    ),
                                                    Name(id='value', ctx=Load()),
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
                Assign(
                    targets=[Name(id='_str_to_monetary', ctx=Store())],
                    value=Name(id='_str_to_float', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_str_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='value', ctx=Load()),
                                    List(elts=[], ctx=Load()),
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
                Assign(
                    targets=[
                        Name(id='_str_to_reference', ctx=Store()),
                        Name(id='_str_to_char', ctx=Store()),
                        Name(id='_str_to_text', ctx=Store()),
                        Name(id='_str_to_binary', ctx=Store()),
                        Name(id='_str_to_html', ctx=Store()),
                    ],
                    value=Name(id='_str_id', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_str_to_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='parsed_value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='parsed_value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_format_import_error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="'%s' does not seem to be a valid date for field '%%(field)s'", kind='u')],
                                                        keywords=[],
                                                    ),
                                                    Name(id='value', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='moreinfo', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value="Use the format '%s'", kind='u'),
                                                                    Constant(value='2012-12-31', kind='u'),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                    name='_input_tz',
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
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tz', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pytz', ctx=Load()),
                                                    attr='timezone',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_context',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='tz', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='pytz', ctx=Load()),
                                                attr='UnknownTimeZoneError',
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
                            orelse=[],
                        ),
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
                        If(
                            test=Attribute(
                                value=Name(id='user', ctx=Load()),
                                attr='tz',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pytz', ctx=Load()),
                                                    attr='timezone',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='pytz', ctx=Load()),
                                                attr='UnknownTimeZoneError',
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
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='pytz', ctx=Load()),
                                attr='UTC',
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
                    name='_str_to_datetime',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='parsed_value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_format_import_error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="'%s' does not seem to be a valid datetime for field '%%(field)s'", kind='u')],
                                                        keywords=[],
                                                    ),
                                                    Name(id='value', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='moreinfo', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value="Use the format '%s'", kind='u'),
                                                                    Constant(value='2012-12-31 23:59:59', kind='u'),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                            targets=[Name(id='input_tz', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_input_tz',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='input_tz', ctx=Load()),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='parsed_value', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='is_dst',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='dt', ctx=Load()),
                                                    attr='astimezone',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='pytz', ctx=Load()),
                                                        attr='UTC',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(elts=[], ctx=Load()),
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
                    name='_get_translations',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='types', annotation=None, type_comment=None),
                            arg(arg='src', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='types', ctx=Store())],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[Name(id='types', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tnx_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        attr='cache',
                                        ctx=Load(),
                                    ),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
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
                                            value=Name(id='tnx_cache', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='types', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Name(id='src', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='tnx_cache', ctx=Load()),
                                                slice=Name(id='types', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='tnx_cache', ctx=Load()),
                                            slice=Name(id='types', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='src', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Translations', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.translation', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tnx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Translations', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='types', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='src', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='src', ctx=Load()),
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
                                Name(id='result', ctx=Store()),
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='tnx_cache', ctx=Load()),
                                        slice=Name(id='types', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='src', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='value',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='t', ctx=Store()),
                                        iter=Name(id='tnx', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='t', ctx=Load()),
                                                    attr='value',
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
                    name='_str_to_selection',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
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
                            targets=[Name(id='env', ctx=Store())],
                            value=Attribute(
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
                                attr='env',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='selection', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='get_description',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='env', ctx=Load())],
                                    keywords=[],
                                ),
                                slice=Constant(value='selection', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='item', ctx=Store()),
                                    Name(id='label', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='selection', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='label', ctx=Store())],
                                    value=Call(
                                        func=Name(id='ustr', ctx=Load()),
                                        args=[Name(id='label', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='labels', ctx=Store())],
                                    value=BinOp(
                                        left=List(
                                            elts=[Name(id='label', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_translations',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='selection', kind=None),
                                                        Constant(value='model', kind=None),
                                                        Constant(value='code', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Name(id='label', ctx=Load()),
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
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='value', ctx=Load()),
                                                        attr='lower',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='item', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='lower',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Name(id='value', ctx=Load()),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='label', ctx=Load()),
                                                                        attr='lower',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='label', ctx=Store()),
                                                                iter=Name(id='labels', ctx=Load()),
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
                                            value=Tuple(
                                                elts=[
                                                    Name(id='item', ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                ctx=Load(),
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
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
                                        args=[
                                            Constant(value='import_skip_records', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
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
                                                args=[
                                                    Constant(value='import_set_empty_fields', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Raise(
                            exc=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_import_error',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ValueError', ctx=Load()),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value="Value '%s' not found in selection field '%%(field)s'", kind='u')],
                                        keywords=[],
                                    ),
                                    Name(id='value', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='moreinfo', kind=None)],
                                        values=[
                                            ListComp(
                                                elt=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='_label', ctx=Load()),
                                                        Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='item', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='item', ctx=Store()),
                                                                Name(id='_label', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Name(id='selection', ctx=Load()),
                                                        ifs=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='_label', ctx=Load()),
                                                                    Name(id='item', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
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
                    name='db_id_for',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='subfield', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Finds a database id for the reference ``value`` in the referencing\n        subfield ``subfield`` of the provided field of the provided model.\n\n        :param model: model to which the field belongs\n        :param field: relational field for which references are provided\n        :param subfield: a relational subfield allowing building of refs to\n                         existing records: ``None`` for a name_get/name_search,\n                         ``id`` for an external id and ``.id`` for a database\n                         id\n        :param value: value of the reference to match to an actual record\n        :param context: OpenERP request context\n        :return: a pair of the matched database identifier (if any), the\n                 translated user-readable name for the field and the list of\n                 warnings\n        :rtype: (ID|None, unicode, list)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='flush', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='import_flush', kind=None),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=arg(arg='kw', annotation=None, type_comment=None),
                                            defaults=[],
                                        ),
                                        body=Constant(value=None, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='warnings', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='error_msg', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='help', kind=None),
                                ],
                                values=[
                                    Constant(value='Possible Values', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='new', kind=None),
                                    Constant(value='tree,form', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='list', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                    Dict(
                                        keys=[Constant(value='create', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='See all possible values', kind='u')],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='subfield', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='res_model', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='comodel_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='subfield', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='.id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='res_model', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='ir.model.data', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='domain', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='comodel_name',
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='RelatedModel', ctx=Store())],
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
                        If(
                            test=Compare(
                                left=Name(id='subfield', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='.id', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='field_type', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='database id', kind='u')],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='value', ctx=Load()),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_str_to_boolean',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='model', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                            Name(id='value', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Name(id='field_type', ctx=Load()),
                                                    Name(id='warnings', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='tentative_id', ctx=Store())],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tentative_id', ctx=Store())],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Try(
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='RelatedModel', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='tentative_id', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='id', ctx=Store())],
                                                    value=Name(id='tentative_id', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='psycopg2', ctx=Load()),
                                                attr='DataError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_format_import_error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='ValueError', ctx=Load()),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value="Invalid database id '%s' for the field '%%(field)s'", kind='u')],
                                                                keywords=[],
                                                            ),
                                                            Name(id='value', ctx=Load()),
                                                            Dict(
                                                                keys=[Constant(value='moreinfo', kind=None)],
                                                                values=[Name(id='action', ctx=Load())],
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
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='subfield', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='id', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field_type', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='external id', kind='u')],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_str_to_boolean',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='model', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                            Name(id='value', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Return(
                                                    value=Tuple(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Name(id='field_type', ctx=Load()),
                                                            Name(id='warnings', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Constant(value='.', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='value', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='xmlid', ctx=Store())],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='xmlid', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='%s.%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
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
                                                                    args=[
                                                                        Constant(value='_import_current_module', kind=None),
                                                                        Constant(value='', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                Name(id='value', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='flush', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='xml_id',
                                                        value=Name(id='xmlid', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_xmlid_to_record_id',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='xmlid', ctx=Load()),
                                                    Name(id='RelatedModel', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='subfield', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='field_type', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='name', kind='u')],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='value', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='', kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Tuple(
                                                                elts=[
                                                                    Constant(value=False, kind=None),
                                                                    Name(id='field_type', ctx=Load()),
                                                                    Name(id='warnings', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='flush', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='model',
                                                                value=Attribute(
                                                                    value=Name(id='field', ctx=Load()),
                                                                    attr='comodel_name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='ids', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='RelatedModel', ctx=Load()),
                                                            attr='name_search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Name(id='value', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='operator',
                                                                value=Constant(value='=', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='ids', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='ids', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='warnings', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='ImportWarning', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Call(
                                                                                            func=Name(id='_', ctx=Load()),
                                                                                            args=[Constant(value="Found multiple matches for value '%s' in field '%%(field)s' (%d matches)", kind='u')],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Name(id='value', ctx=Load()),
                                                                                                Call(
                                                                                                    func=Name(id='len', ctx=Load()),
                                                                                                    args=[Name(id='ids', ctx=Load())],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
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
                                                        Assign(
                                                            targets=[
                                                                Tuple(
                                                                    elts=[
                                                                        Name(id='id', ctx=Store()),
                                                                        Name(id='_name', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='ids', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='name_create_enabled_fields', ctx=Store())],
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Call(
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
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='name_create_enabled_fields', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Dict(keys=[], values=[]),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Call(
                                                                func=Attribute(
                                                                    value=Name(id='name_create_enabled_fields', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Try(
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Tuple(
                                                                                    elts=[
                                                                                        Name(id='id', ctx=Store()),
                                                                                        Name(id='_name', ctx=Store()),
                                                                                    ],
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='RelatedModel', ctx=Load()),
                                                                                    attr='name_create',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='name',
                                                                                        value=Name(id='value', ctx=Load()),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    handlers=[
                                                                        ExceptHandler(
                                                                            type=Tuple(
                                                                                elts=[
                                                                                    Name(id='Exception', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='psycopg2', ctx=Load()),
                                                                                        attr='IntegrityError',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            name=None,
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='error_msg', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[
                                                                                            Constant(value="Cannot create new '%s' records from their name alone. Please create those records manually and try importing again.", kind='u'),
                                                                                            Attribute(
                                                                                                value=Name(id='RelatedModel', ctx=Load()),
                                                                                                attr='_description',
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
                                                                    finalbody=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_format_import_error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='Exception', ctx=Load()),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value="Unknown sub-field '%s'", kind='u')],
                                                                keywords=[],
                                                            ),
                                                            Name(id='subfield', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='set_empty', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='skip_record', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
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
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='import_file', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='import_set_empty_fields', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
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
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='import_set_empty_fields', kind=None)],
                                                keywords=[],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field_path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='/', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
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
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='parent_fields_hierarchy', kind=None),
                                                        List(elts=[], ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=List(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='name',
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
                                Assign(
                                    targets=[Name(id='set_empty', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='field_path', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='import_set_empty_fields', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='skip_record', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='field_path', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Call(
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
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='import_skip_records', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='id', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='set_empty', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='skip_record', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Name(id='error_msg', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="No matching record found for %(field_type)s '%(value)s' in field '%%(field)s' and the following error was encountered when we attempted to create one: %(error_message)s", kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="No matching record found for %(field_type)s '%(value)s' in field '%%(field)s'", kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='error_info_dict', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='moreinfo', kind=None)],
                                        values=[Name(id='action', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
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
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='import_file', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=IfExp(
                                                test=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='value', ctx=Load()),
                                                        Name(id='str', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                body=Subscript(
                                                    value=Name(id='value', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=50, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                orelse=Name(id='value', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='error_info_dict', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='value', kind=None),
                                                            Constant(value='field_type', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='value', ctx=Load()),
                                                            Name(id='field_type', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Name(id='error_msg', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error_info_dict', ctx=Load()),
                                                            slice=Constant(value='error_message', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='error_msg', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_format_import_error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ValueError', ctx=Load()),
                                            Name(id='message', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='field_type', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='error_message', kind=None),
                                                ],
                                                values=[
                                                    Name(id='field_type', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
                                                    Name(id='error_msg', ctx=Load()),
                                                ],
                                            ),
                                            Name(id='error_info_dict', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='id', ctx=Load()),
                                    Name(id='field_type', ctx=Load()),
                                    Name(id='warnings', ctx=Load()),
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
                    name='_xmlid_to_record_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xmlid', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the record id corresponding to the given external id,\n        provided that the record actually exists; otherwise return ``None``.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='import_cache', ctx=Store())],
                            value=Call(
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
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='import_cache', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='import_cache', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xmlid', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='result', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='module', ctx=Store()),
                                                Name(id='name', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xmlid', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='\n                SELECT d.model, d.res_id\n                FROM ir_model_data d\n                JOIN "{}" r ON d.res_id = r.id\n                WHERE d.module = %s AND d.name = %s\n            ', kind=None),
                                            attr='format',
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
                                            List(
                                                elts=[
                                                    Name(id='module', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='result', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='res_model', ctx=Store()),
                                                Name(id='res_id', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        Subscript(
                                            value=Name(id='import_cache', ctx=Load()),
                                            slice=Name(id='xmlid', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='result', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='res_model', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='MSG', ctx=Store())],
                                            value=Constant(value='Invalid external ID %s: expected model %r, found %r', kind=None),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='MSG', ctx=Load()),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='xmlid', ctx=Load()),
                                                                Attribute(
                                                                    value=Name(id='model', ctx=Load()),
                                                                    attr='_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='res_model', ctx=Load()),
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
                                Return(
                                    value=Name(id='res_id', ctx=Load()),
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
                    name='_referencing_subfield',
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
                            value=Constant(value=' Checks the record for the subfields allowing referencing (an\n        existing record in an other table), errors out if it finds potential\n        conflicts (multiple referencing subfields) or non-referencing subfields\n        returns the name of the correct subfield.\n\n        :param record:\n        :return: the record subfield to use for referencing and a list of warnings\n        :rtype: str, list\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='fieldset', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BinOp(
                                left=Name(id='fieldset', ctx=Load()),
                                op=Sub(),
                                right=Name(id='REFERENCING_FIELDS', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Can not create Many-To-One records indirectly, import the field separately', kind='u')],
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
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='fieldset', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Ambiguous specification for field '%(field)s', only provide one of name, external id or database id", kind='u')],
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
                            targets=[
                                List(
                                    elts=[Name(id='subfield', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='fieldset', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='subfield', ctx=Load()),
                                    List(elts=[], ctx=Load()),
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
                    name='_str_to_many2one',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
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
                            targets=[
                                List(
                                    elts=[Name(id='record', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='values', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='subfield', ctx=Store()),
                                        Name(id='w1', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_referencing_subfield',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='id', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='w2', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='db_id_for',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                    Name(id='subfield', ctx=Load()),
                                    Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Name(id='subfield', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='id', ctx=Load()),
                                    BinOp(
                                        left=Name(id='w1', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='w2', ctx=Load()),
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
                    name='_str_to_many2one_reference',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_str_to_integer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                    Name(id='value', ctx=Load()),
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
                    name='_str_to_many2many',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
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
                                List(
                                    elts=[Name(id='record', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='subfield', ctx=Store()),
                                        Name(id='warnings', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_referencing_subfield',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='reference', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Name(id='subfield', ctx=Load()),
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
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='id', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                                Name(id='ws', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='db_id_for',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='model', ctx=Load()),
                                            Name(id='field', ctx=Load()),
                                            Name(id='subfield', ctx=Load()),
                                            Name(id='reference', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='warnings', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ws', ctx=Load())],
                                        keywords=[],
                                    ),
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
                                        left=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
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
                                                args=[
                                                    Constant(value='import_set_empty_fields', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Compare(
                                                    left=Name(id='id', ctx=Load()),
                                                    ops=[Is()],
                                                    comparators=[Constant(value=None, kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='id', ctx=Store()),
                                                        iter=Name(id='ids', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='ids', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='id', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='id', ctx=Store()),
                                                iter=Name(id='ids', ctx=Load()),
                                                ifs=[Name(id='id', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
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
                                                        args=[
                                                            Constant(value='import_skip_records', kind=None),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    ListComp(
                                                        elt=Compare(
                                                            left=Name(id='id', ctx=Load()),
                                                            ops=[Is()],
                                                            comparators=[Constant(value=None, kind=None)],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='id', ctx=Store()),
                                                                iter=Name(id='ids', ctx=Load()),
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
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Name(id='warnings', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='update_many2many', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='link',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='id', ctx=Store()),
                                                        iter=Name(id='ids', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            Name(id='warnings', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='warnings', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
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
                    name='_str_to_one2many',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name_create_enabled_fields', ctx=Store())],
                            value=BoolOp(
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
                                        args=[Constant(value='name_create_enabled_fields', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='prefix', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Constant(value='/', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='relative_name_create_enabled_fields', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='k', ctx=Load()),
                                    slice=Slice(
                                        lower=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='prefix', ctx=Load())],
                                            keywords=[],
                                        ),
                                        upper=None,
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
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
                                                value=Name(id='name_create_enabled_fields', ctx=Load()),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='k', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='prefix', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='commands', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='warnings', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='records', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='exclude_ref_fields', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='records', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Dict(keys=[], values=[])],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='records', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='subfield', ctx=Store()),
                                                Name(id='ws', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_referencing_subfield',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='record', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='warnings', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ws', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=GeneratorExp(
                                        elt=Dict(
                                            keys=[Name(id='subfield', ctx=Load())],
                                            values=[Name(id='item', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='item', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='record', ctx=Load()),
                                                            slice=Name(id='subfield', ctx=Load()),
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        FunctionDef(
                            name='log',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='f', annotation=None, type_comment=None),
                                    arg(arg='exception', annotation=None, type_comment=None),
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
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='exception', ctx=Load()),
                                                Name(id='Warning', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='current_field_name', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
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
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='f', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='string',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='arg0', ctx=Store())],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='exception', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Mod(),
                                                right=Dict(
                                                    keys=[Constant(value='field', kind=None)],
                                                    values=[
                                                        BinOp(
                                                            left=Constant(value='%(field)s/', kind=None),
                                                            op=Add(),
                                                            right=Name(id='current_field_name', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='exception', ctx=Load()),
                                                    attr='args',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='arg0', ctx=Load()),
                                                    Starred(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='exception', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Slice(
                                                                lower=Constant(value=1, kind=None),
                                                                upper=None,
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Name(id='exception', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='warnings', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='exception', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='parent_fields_hierarchy', ctx=Store())],
                            value=BinOp(
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
                                    args=[
                                        Constant(value='parent_fields_hierarchy', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='convert', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name_create_enabled_fields',
                                                value=Name(id='relative_name_create_enabled_fields', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='parent_fields_hierarchy',
                                                value=Name(id='parent_fields_hierarchy', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='for_model',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='records', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='id', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='refs', ctx=Store())],
                                    value=Call(
                                        func=Name(id='only_ref_fields', ctx=Load()),
                                        args=[Name(id='record', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='writable', ctx=Store())],
                                    value=Call(
                                        func=Name(id='convert', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='exclude_ref_fields', ctx=Load()),
                                                args=[Name(id='record', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='log', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='refs', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='subfield', ctx=Store()),
                                                        Name(id='w1', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_referencing_subfield',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='refs', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='warnings', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='w1', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='id', ctx=Store()),
                                                                Name(id='_', ctx=Store()),
                                                                Name(id='w2', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='db_id_for',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='model', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                            Name(id='subfield', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='record', ctx=Load()),
                                                                slice=Name(id='subfield', ctx=Load()),
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
                                                            value=Name(id='warnings', ctx=Load()),
                                                            attr='extend',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='w2', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='ValueError', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='subfield', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='id', kind=None)],
                                                            ),
                                                            body=[Raise(exc=None, cause=None)],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='writable', ctx=Load()),
                                                                    slice=Constant(value='id', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='record', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
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
                                If(
                                    test=Name(id='id', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='commands', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='link',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='commands', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='id', ctx=Load()),
                                                            Name(id='writable', ctx=Load()),
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
                                                    value=Name(id='commands', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='writable', ctx=Load())],
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
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='commands', ctx=Load()),
                                    Name(id='warnings', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='O2MIdMapper',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Updates the base class to support setting xids directly in create by\n    providing an "id" key (otherwise stripped by create) during an import\n    (which should strip \'id\' from the input data anyway)\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='base', kind=None),
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
                            targets=[Name(id='recs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
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
                        Assign(
                            targets=[Name(id='import_module', ctx=Store())],
                            value=Call(
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
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='_import_current_module', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='import_module', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='recs', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='noupdate', ctx=Store())],
                            value=Call(
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
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='noupdate', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xids', ctx=Store())],
                            value=GeneratorExp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='v', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='id', kind=None)],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='v', ctx=Store()),
                                        iter=Name(id='vals_list', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
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
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_update_xmlids',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='xml_id', kind=None),
                                                Constant(value='record', kind=None),
                                                Constant(value='noupdate', kind=None),
                                            ],
                                            values=[
                                                IfExp(
                                                    test=Compare(
                                                        left=Constant(value='.', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='xid', ctx=Load())],
                                                    ),
                                                    body=Name(id='xid', ctx=Load()),
                                                    orelse=BinOp(
                                                        left=Constant(value='%s.%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='import_module', ctx=Load()),
                                                                Name(id='xid', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                                Name(id='rec', ctx=Load()),
                                                Name(id='noupdate', ctx=Load()),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='rec', ctx=Store()),
                                                        Name(id='xid', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='zip', ctx=Load()),
                                                    args=[
                                                        Name(id='recs', ctx=Load()),
                                                        Name(id='xids', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='xid', ctx=Load()),
                                                            Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='xid', ctx=Load()),
                                                                    Name(id='str', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='recs', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='returns',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='self', kind=None),
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
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
    ],
    type_ignores=[],
)
