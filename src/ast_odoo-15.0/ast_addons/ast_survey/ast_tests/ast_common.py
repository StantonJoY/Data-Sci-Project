Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='Counter', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests.common',
            names=[alias(name='mail_new_test_user', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='SurveyCase',
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
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SurveyCase', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Constant(value=' Some custom stuff to make the matching between questions and answers\n          :param dict _type_match: dict\n            key: question type\n            value: (answer type, answer field_name)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_type_match',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='text_box', kind=None),
                                    Constant(value='char_box', kind=None),
                                    Constant(value='numerical_box', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='simple_choice', kind=None),
                                    Constant(value='multiple_choice', kind=None),
                                    Constant(value='matrix', kind=None),
                                ],
                                values=[
                                    Tuple(
                                        elts=[
                                            Constant(value='text_box', kind=None),
                                            Constant(value='value_text_box', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='char_box', kind=None),
                                            Constant(value='value_char_box', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='numerical_box', kind=None),
                                            Constant(value='value_numerical_box', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Constant(value='value_date', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='suggestion', kind=None),
                                            Constant(value='suggested_answer_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='suggestion', kind=None),
                                            Constant(value='suggested_answer_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='suggestion', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='suggested_answer_id', kind=None),
                                                    Constant(value='matrix_row_id', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertAnswer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
                            arg(arg='state', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='answer', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Name(id='state', ctx=Load()),
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
                                        value=Name(id='answer', ctx=Load()),
                                        attr='last_displayed_page_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='page', ctx=Load()),
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
                    name='assertAnswerLines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
                            arg(arg='answer_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check answer lines.\n\n          :param dict answer_data:\n            key = question ID\n            value = {'value': [user input]}\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='answer', ctx=Load()),
                                        attr='user_input_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='page_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='page', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='answer_count', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='user_input', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='user_input', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='answer_data', ctx=Load()),
                                                        attr='values',
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
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='answer_count', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='qid', ctx=Store()),
                                    Name(id='user_input', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='answer_data', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='answer_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='l', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='l', ctx=Load()),
                                                            attr='question_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='qid', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='question', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Name(id='answer_lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='question_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='question_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='multiple_choice', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='user_input', ctx=Load()),
                                                slice=Constant(value='value', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='answer_fname', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_type_match',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Attribute(
                                                        value=Name(id='question', ctx=Load()),
                                                        attr='question_type',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
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
                                                    Call(
                                                        func=Name(id='Counter', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Attribute(
                                                                    value=Call(
                                                                        func=Name(id='getattr', ctx=Load()),
                                                                        args=[
                                                                            Name(id='line', ctx=Load()),
                                                                            Name(id='answer_fname', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='line', ctx=Store()),
                                                                        iter=Name(id='answer_lines', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='Counter', ctx=Load()),
                                                        args=[Name(id='values', ctx=Load())],
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
                                                left=Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='question_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='simple_choice', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        List(
                                                            elts=[Name(id='value', ctx=Store())],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='user_input', ctx=Load()),
                                                        slice=Constant(value='value', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='answer_fname', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_type_match',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Attribute(
                                                                value=Name(id='question', ctx=Load()),
                                                                attr='question_type',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
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
                                                                value=Call(
                                                                    func=Name(id='getattr', ctx=Load()),
                                                                    args=[
                                                                        Name(id='answer_lines', ctx=Load()),
                                                                        Name(id='answer_fname', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='value', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='question', ctx=Load()),
                                                            attr='question_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='matrix', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                List(
                                                                    elts=[
                                                                        Name(id='value_col', ctx=Store()),
                                                                        Name(id='value_row', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='user_input', ctx=Load()),
                                                                slice=Constant(value='value', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='answer_fname_col', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_type_match',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Attribute(
                                                                            value=Name(id='question', ctx=Load()),
                                                                            attr='question_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='answer_fname_row', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_type_match',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Attribute(
                                                                            value=Name(id='question', ctx=Load()),
                                                                            attr='question_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=1, kind=None),
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
                                                                        value=Call(
                                                                            func=Name(id='getattr', ctx=Load()),
                                                                            args=[
                                                                                Name(id='answer_lines', ctx=Load()),
                                                                                Name(id='answer_fname_col', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='value_col', ctx=Load()),
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
                                                                        value=Call(
                                                                            func=Name(id='getattr', ctx=Load()),
                                                                            args=[
                                                                                Name(id='answer_lines', ctx=Load()),
                                                                                Name(id='answer_fname_row', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='value_row', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                List(
                                                                    elts=[Name(id='value', ctx=Store())],
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='user_input', ctx=Load()),
                                                                slice=Constant(value='value', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='answer_fname', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_type_match',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Attribute(
                                                                        value=Name(id='question', ctx=Load()),
                                                                        attr='question_type',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='question', ctx=Load()),
                                                                    attr='question_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='numerical_box', kind=None)],
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
                                                                                func=Name(id='getattr', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='answer_lines', ctx=Load()),
                                                                                    Name(id='answer_fname', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            Call(
                                                                                func=Name(id='float', ctx=Load()),
                                                                                args=[Name(id='value', ctx=Load())],
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
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='assertEqual',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='getattr', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='answer_lines', ctx=Load()),
                                                                                    Name(id='answer_fname', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            Name(id='value', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
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
                    name='assertResponse',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='response', annotation=None, type_comment=None),
                            arg(arg='status_code', annotation=None, type_comment=None),
                            arg(arg='text_bits', annotation=None, type_comment=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Name(id='status_code', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='text', ctx=Store()),
                            iter=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='text_bits', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='text', ctx=Load()),
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='text',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_question',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='qtype', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='constr_mandatory', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='constr_mandatory', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='constr_error_msg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='constr_error_msg', kind=None),
                                    Constant(value='TestError', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sequence', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='sequence', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sequence', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sequence', ctx=Store())],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='page', ctx=Load()),
                                            attr='question_ids',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='page', ctx=Load()),
                                                        attr='question_ids',
                                                        ctx=Load(),
                                                    ),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='sequence',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        orelse=BinOp(
                                            left=Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='sequence',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='base_qvalues', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='sequence', kind=None),
                                    Constant(value='title', kind=None),
                                    Constant(value='question_type', kind=None),
                                    Constant(value='constr_mandatory', kind=None),
                                    Constant(value='constr_error_msg', kind=None),
                                ],
                                values=[
                                    Name(id='sequence', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='qtype', ctx=Load()),
                                    Name(id='constr_mandatory', ctx=Load()),
                                    Name(id='constr_error_msg', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='qtype', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='simple_choice', kind=None),
                                            Constant(value='multiple_choice', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='base_qvalues', ctx=Load()),
                                            slice=Constant(value='suggested_answer_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Dict(
                                                    keys=[
                                                        Constant(value='value', kind=None),
                                                        Constant(value='answer_score', kind=None),
                                                        Constant(value='is_correct', kind=None),
                                                    ],
                                                    values=[
                                                        Subscript(
                                                            value=Name(id='label', ctx=Load()),
                                                            slice=Constant(value='value', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='label', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='answer_score', kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='label', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='is_correct', kind=None),
                                                                Constant(value=False, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='label', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='kwargs', ctx=Load()),
                                                        attr='pop',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='labels', kind=None)],
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
                                    test=Compare(
                                        left=Name(id='qtype', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='matrix', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='base_qvalues', ctx=Load()),
                                                    slice=Constant(value='matrix_subtype', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='matrix_subtype', kind=None),
                                                    Constant(value='simple', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='base_qvalues', ctx=Load()),
                                                    slice=Constant(value='suggested_answer_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Subscript(
                                                                    value=Name(id='label', ctx=Load()),
                                                                    slice=Constant(value='value', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='label', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='answer_score', kind=None),
                                                                        Constant(value=0, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='label', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='kwargs', ctx=Load()),
                                                                attr='pop',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='labels', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='base_qvalues', ctx=Load()),
                                                    slice=Constant(value='matrix_row_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='answer_score', kind=None),
                                                            ],
                                                            values=[
                                                                Subscript(
                                                                    value=Name(id='label', ctx=Load()),
                                                                    slice=Constant(value='value', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='label', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='answer_score', kind=None),
                                                                        Constant(value=0, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='label', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='kwargs', ctx=Load()),
                                                                attr='pop',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='labels_2', kind=None)],
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
                                    orelse=[Pass()],
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base_qvalues', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='kwargs', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='question', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='base_qvalues', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='question', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_answer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='base_avals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='survey_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='email', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Name(id='partner', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='email', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base_avals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='kwargs', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='base_avals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_answer_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
                            arg(arg='answer_value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='qtype', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_type_match',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='question', ctx=Load()),
                                        attr='question_type',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='answer_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='answer_type', kind=None),
                                    Subscript(
                                        value=Name(id='qtype', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='answer_fname', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='answer_fname', kind=None),
                                    Subscript(
                                        value=Name(id='qtype', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_alvals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='user_input_id', kind=None),
                                    Constant(value='question_id', kind=None),
                                    Constant(value='skipped', kind=None),
                                    Constant(value='answer_type', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='answer', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='question', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Name(id='answer_type', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='base_alvals', ctx=Load()),
                                    slice=Name(id='answer_fname', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='answer_value', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base_alvals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='kwargs', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='survey.user_input.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='base_alvals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_access_start',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
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
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/start/%s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='survey', ctx=Load()),
                                            attr='access_token',
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
                    name='_access_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
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
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='survey', ctx=Load()),
                                                    attr='access_token',
                                                    ctx=Load(),
                                                ),
                                                Name(id='token', ctx=Load()),
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
                    name='_access_begin',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='get_base_url',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Constant(value='/survey/begin/%s/%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='access_token',
                                                ctx=Load(),
                                            ),
                                            Name(id='token', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Name(id='url', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='json',
                                        value=Dict(keys=[], values=[]),
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
                    name='_access_submit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='survey', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='post_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='survey', ctx=Load()),
                                        attr='get_base_url',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Constant(value='/survey/submit/%s/%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='survey', ctx=Load()),
                                                attr='access_token',
                                                ctx=Load(),
                                            ),
                                            Name(id='token', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Name(id='url', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='json',
                                        value=Dict(
                                            keys=[Constant(value='params', kind=None)],
                                            values=[Name(id='post_data', ctx=Load())],
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
                    name='_find_csrf_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='csrf_token_re', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='compile',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(input.+csrf_token.+value=")([a-f0-9]{40}o[0-9]*)', kind=None),
                                    Attribute(
                                        value=Name(id='re', ctx=Load()),
                                        attr='MULTILINE',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='csrf_token_re', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='text', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='groups',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_post_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                            arg(arg='answers', annotation=None, type_comment=None),
                            arg(arg='post_data', annotation=None, type_comment=None),
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
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='answers', ctx=Load()),
                                        Name(id='list', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=Name(id='answers', ctx=Load()),
                                orelse=List(
                                    elts=[Name(id='answers', ctx=Load())],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='question_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='multiple_choice', kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='value', ctx=Store()),
                                    iter=Name(id='values', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='question', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='post_data', ctx=Load())],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='post_data', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='question', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
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
                                                                    value=Subscript(
                                                                        value=Name(id='post_data', ctx=Load()),
                                                                        slice=Attribute(
                                                                            value=Name(id='question', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='value', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='post_data', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='question', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=List(
                                                                elts=[
                                                                    Subscript(
                                                                        value=Name(id='post_data', ctx=Load()),
                                                                        slice=Attribute(
                                                                            value=Name(id='question', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='value', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='post_data', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='question', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        List(
                                            elts=[Name(id='values', ctx=Store())],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='values', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='post_data', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='post_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_answer_question',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                            arg(arg='csrf_token', annotation=None, type_comment=None),
                            arg(arg='button_submit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='next', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='post_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_submission_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='question', ctx=Load()),
                                    Name(id='answer', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='csrf_token', kind=None),
                                            Constant(value='token', kind=None),
                                            Constant(value='button_submit', kind=None),
                                        ],
                                        values=[
                                            Name(id='csrf_token', ctx=Load()),
                                            Name(id='answer_token', ctx=Load()),
                                            Name(id='button_submit', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_submit',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='question', ctx=Load()),
                                        attr='survey_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='answer_token', ctx=Load()),
                                    Name(id='post_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_page',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='question', ctx=Load()),
                                        attr='survey_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
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
                    name='_answer_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='answers', annotation=None, type_comment=None),
                            arg(arg='answer_token', annotation=None, type_comment=None),
                            arg(arg='csrf_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='post_data', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='question', ctx=Store()),
                                    Name(id='answer', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='answers', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='post_data', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='question', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='answer', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='post_data', ctx=Load()),
                                    slice=Constant(value='page_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='page', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='post_data', ctx=Load()),
                                    slice=Constant(value='csrf_token', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='csrf_token', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='post_data', ctx=Load()),
                                    slice=Constant(value='token', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='answer_token', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_submit',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='page', ctx=Load()),
                                        attr='survey_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='answer_token', ctx=Load()),
                                    Name(id='post_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_access_page',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='page', ctx=Load()),
                                        attr='survey_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='answer_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertResponse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value=200, kind=None),
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
                    name='_format_submission_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
                            arg(arg='additional_post_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='post_data', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='post_data', ctx=Load()),
                                    slice=Constant(value='question_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='question', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post_data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_post_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='question', ctx=Load()),
                                            Name(id='answer', ctx=Load()),
                                            Name(id='post_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='question', ctx=Load()),
                                attr='page_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='post_data', ctx=Load()),
                                            slice=Constant(value='page_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='question', ctx=Load()),
                                            attr='page_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post_data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='additional_post_data', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='post_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_assert_skipped_question',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='question', annotation=None, type_comment=None),
                            arg(arg='survey_user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='statistics', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='question', ctx=Load()),
                                    attr='_prepare_statistics',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='survey_user', ctx=Load()),
                                        attr='user_input_line_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='question_data', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='question_data', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='question_data', ctx=Store()),
                                                iter=Name(id='statistics', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='question_data', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='question', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='question', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value=False, kind=None),
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
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='question_data', ctx=Load())],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='question_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='answer_input_skipped_ids', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                    name='_create_one_question_per_type',
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
                            targets=[Name(id='all_questions', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='survey.question', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='question_type', ctx=Store()),
                                    Name(id='dummy', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='survey.question', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_fields',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='question_type', kind=None),
                                    ctx=Load(),
                                ),
                                attr='selection',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='kwargs', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='question_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='multiple_choice', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    slice=Constant(value='labels', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Dict(
                                                        keys=[Constant(value='value', kind=None)],
                                                        values=[Constant(value='MChoice0', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='value', kind=None)],
                                                        values=[Constant(value='MChoice1', kind=None)],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='question_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='simple_choice', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='kwargs', ctx=Load()),
                                                            slice=Constant(value='labels', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=List(elts=[], ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='question_type', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='matrix', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='kwargs', ctx=Load()),
                                                                    slice=Constant(value='labels', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[Constant(value='value', kind=None)],
                                                                        values=[Constant(value='Column0', kind=None)],
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='value', kind=None)],
                                                                        values=[Constant(value='Column1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='kwargs', ctx=Load()),
                                                                    slice=Constant(value='labels_2', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[Constant(value='value', kind=None)],
                                                                        values=[Constant(value='Row0', kind=None)],
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='value', kind=None)],
                                                                        values=[Constant(value='Row1', kind=None)],
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
                                    ],
                                ),
                                AugAssign(
                                    target=Name(id='all_questions', ctx=Store()),
                                    op=BitOr(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_question',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='page_0',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Q0', kind=None),
                                            Name(id='question_type', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='all_questions', ctx=Load()),
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
            name='TestSurveyCommon',
            bases=[Name(id='SurveyCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestSurveyCommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Constant(value=' Create test data: a survey with some pre-defined questions and various test users for ACL ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey_manager',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Gustave Doré', kind=None),
                                    ),
                                    keyword(
                                        arg='login',
                                        value=Constant(value='survey_manager', kind=None),
                                    ),
                                    keyword(
                                        arg='email',
                                        value=Constant(value='survey.manager@example.com', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='survey.group_survey_manager,base.group_user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey_user',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Lukas Peeters', kind=None),
                                    ),
                                    keyword(
                                        arg='login',
                                        value=Constant(value='survey_user', kind=None),
                                    ),
                                    keyword(
                                        arg='email',
                                        value=Constant(value='survey.user@example.com', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='survey.group_survey_user,base.group_user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_emp',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Eglantine Employee', kind=None),
                                    ),
                                    keyword(
                                        arg='login',
                                        value=Constant(value='user_emp', kind=None),
                                    ),
                                    keyword(
                                        arg='email',
                                        value=Constant(value='employee@example.com', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_user', kind=None),
                                    ),
                                    keyword(
                                        arg='password',
                                        value=Constant(value='user_emp', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_portal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Patrick Portal', kind=None),
                                    ),
                                    keyword(
                                        arg='login',
                                        value=Constant(value='user_portal', kind=None),
                                    ),
                                    keyword(
                                        arg='email',
                                        value=Constant(value='portal@example.com', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_portal', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_public',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Pauline Public', kind=None),
                                    ),
                                    keyword(
                                        arg='login',
                                        value=Constant(value='user_public', kind=None),
                                    ),
                                    keyword(
                                        arg='email',
                                        value=Constant(value='public@example.com', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_public', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
                                    ctx=Store(),
                                ),
                            ],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Caroline Customer', kind=None),
                                            Constant(value='customer@example.com', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey',
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
                                                slice=Constant(value='survey.survey', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='survey_manager',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='access_mode', kind=None),
                                            Constant(value='users_login_required', kind=None),
                                            Constant(value='users_can_go_back', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Survey', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='page_0',
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
                                                slice=Constant(value='survey.question', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='survey_manager',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='is_page', kind=None),
                                        ],
                                        values=[
                                            Constant(value='First page', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='survey',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                            Constant(value=True, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='question_ft',
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
                                                slice=Constant(value='survey.question', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='survey_manager',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Free Text', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='survey',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                            Constant(value='text_box', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='question_num',
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
                                                slice=Constant(value='survey.question', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='survey_manager',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='survey_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='question_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test NUmerical Box', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='survey',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=3, kind=None),
                                            Constant(value='numerical_box', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
