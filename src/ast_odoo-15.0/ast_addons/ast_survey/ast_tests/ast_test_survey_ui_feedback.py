Module(
    body=[
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='HttpCaseWithUserDemo', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestUiFeedback',
            bases=[Name(id='HttpCaseWithUserDemo', ctx=Load())],
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
                                            Name(id='TestUiFeedback', ctx=Load()),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey_feedback',
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
                                        slice=Constant(value='survey.survey', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='access_token', kind=None),
                                            Constant(value='access_mode', kind=None),
                                            Constant(value='users_can_go_back', kind=None),
                                            Constant(value='questions_layout', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='question_and_page_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='User Feedback Form', kind=None),
                                            Constant(value='b137640d-14d4-4748-9ef6-344caaaaaae', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='page_per_section', kind=None),
                                            Constant(value='<p>This survey allows you to give a feedback about your experience with our eCommerce solution.\n    Filling it helps us improving your experience.</p></field>', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='is_page', kind=None),
                                                                    Constant(value='description', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='General information', kind=None),
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value='<p>This section is about general information about you. Answering them helps qualifying your answers.</p>', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='constr_mandatory', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Where do you live ?', kind=None),
                                                                    Constant(value=2, kind=None),
                                                                    Constant(value='char_box', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='description', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='When is your date of birth ?', kind=None),
                                                                    Constant(value=3, kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='comments_allowed', kind=None),
                                                                    Constant(value='comment_count_as_answer', kind=None),
                                                                    Constant(value='constr_mandatory', kind=None),
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='How frequently do you buy products online ?', kind=None),
                                                                    Constant(value=4, kind=None),
                                                                    Constant(value='simple_choice', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Once a day', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Once a week', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Once a month', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Once a year', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Other (answer in comment)', kind=None),
                                                                                            Constant(value=5, kind=None),
                                                                                        ],
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
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='constr_mandatory', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='How many times did you order products on our website ?', kind=None),
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value='numerical_box', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='is_page', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='description', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='About our ecommerce', kind=None),
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value='<p>This section is about our eCommerce experience itself.</p>', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='constr_mandatory', kind=None),
                                                                    Constant(value='comments_allowed', kind=None),
                                                                    Constant(value='comment_count_as_answer', kind=None),
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Which of the following words would you use to describe our products ?', kind=None),
                                                                    Constant(value=7, kind=None),
                                                                    Constant(value='multiple_choice', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='High quality', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Useful', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Unique', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Good value for money', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Overpriced', kind=None),
                                                                                            Constant(value=5, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Impractical', kind=None),
                                                                                            Constant(value=6, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Ineffective', kind=None),
                                                                                            Constant(value=7, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Poor quality', kind=None),
                                                                                            Constant(value=8, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Other', kind=None),
                                                                                            Constant(value=9, kind=None),
                                                                                        ],
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
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='matrix_subtype', kind=None),
                                                                    Constant(value='constr_mandatory', kind=None),
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                    Constant(value='matrix_row_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='What do your think about our new eCommerce ?', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value='matrix', kind=None),
                                                                    Constant(value='multiple', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Totally disagree', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Disagree', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Agree', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Totally agree', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                        ],
                                                                                    ),
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
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='The new layout and design is fresh and up-to-date', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='It is easy to find the product that I want', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='The tool to compare the products is useful to make a choice', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='The checkout process is clear and secure', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='I have added products to my wishlist', kind=None),
                                                                                            Constant(value=5, kind=None),
                                                                                        ],
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
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='constr_mandatory', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Do you have any other comments, questions, or concerns ?', kind=None),
                                                                    Constant(value=9, kind=None),
                                                                    Constant(value='text_box', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_admin_survey_tour',
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
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey_feedback',
                                    ctx=Load(),
                                ),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/start/%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='access_token', ctx=Load()),
                                    ),
                                    Constant(value='test_survey', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='admin', kind=None),
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
                    name='test_02_demo_survey_tour',
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
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey_feedback',
                                    ctx=Load(),
                                ),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/start/%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='access_token', ctx=Load()),
                                    ),
                                    Constant(value='test_survey', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='demo', kind=None),
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
                    name='test_03_public_survey_tour',
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
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey_feedback',
                                    ctx=Load(),
                                ),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/start/%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='access_token', ctx=Load()),
                                    ),
                                    Constant(value='test_survey', kind=None),
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
                    name='test_06_survey_prefill',
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
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='survey_feedback',
                                    ctx=Load(),
                                ),
                                attr='access_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/survey/start/%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='access_token', ctx=Load()),
                                    ),
                                    Constant(value='test_survey_prefill', kind=None),
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
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tests',
                                ctx=Load(),
                            ),
                            attr='common',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
