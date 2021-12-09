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
            name='TestUiCertification',
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
                                            Name(id='TestUiCertification', ctx=Load()),
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
                                    attr='survey_certification',
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
                                            Constant(value='users_login_required', kind=None),
                                            Constant(value='scoring_type', kind=None),
                                            Constant(value='certification', kind=None),
                                            Constant(value='certification_mail_template_id', kind=None),
                                            Constant(value='is_time_limited', kind=None),
                                            Constant(value='time_limit', kind=None),
                                            Constant(value='is_attempts_limited', kind=None),
                                            Constant(value='attempts_limit', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='question_and_page_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MyCompany Vendor Certification', kind=None),
                                            Constant(value='4ead4bc8-b8f2-4760-a682-1fde8daaaaac', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='scoring_with_answers', kind=None),
                                            Constant(value=True, kind=None),
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
                                                    args=[Constant(value='survey.mail_template_certification', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='limited', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value='&lt;p&gt;Test your vendor skills!.&lt;/p&gt;', kind=None),
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
                                                                    Constant(value='is_page', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='description', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Products', kind=None),
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value='&lt;p&gt;Test your knowledge of your products!&lt;/p&gt;', kind=None),
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
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Do we sell Acoustic Bloc Screens?', kind=None),
                                                                    Constant(value=2, kind=None),
                                                                    Constant(value='simple_choice', kind=None),
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
                                                                                            Constant(value='No', kind=None),
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
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Yes', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                            Constant(value=2, kind=None),
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
                                                                    Constant(value='column_nb', kind=None),
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Select all the existing products', kind=None),
                                                                    Constant(value=3, kind=None),
                                                                    Constant(value='multiple_choice', kind=None),
                                                                    Constant(value='4', kind=None),
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
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Chair floor protection', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Fanta', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
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
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Conference chair', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Drawer', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Customizable Lamp', kind=None),
                                                                                            Constant(value=5, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
                                                                                            ),
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
                                                                    Constant(value='column_nb', kind=None),
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Select all the available customizations for our Customizable Desk', kind=None),
                                                                    Constant(value=4, kind=None),
                                                                    Constant(value='multiple_choice', kind=None),
                                                                    Constant(value='4', kind=None),
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
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Color', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Height', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
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
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Width', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Legs', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Number of drawers', kind=None),
                                                                                            Constant(value=5, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
                                                                                            ),
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
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='How many versions of the Corner Desk do we have?', kind=None),
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value='simple_choice', kind=None),
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
                                                                                            Constant(value=1, kind=None),
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
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=2, kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value=3, kind=None),
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
                                                                                            Constant(value=4, kind=None),
                                                                                            Constant(value=4, kind=None),
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
                                                                ],
                                                                values=[
                                                                    Constant(value='Do you think we have missing products in our catalog? (not rated)', kind=None),
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value='text_box', kind=None),
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
                                                                    Constant(value='Prices', kind=None),
                                                                    Constant(value=7, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value='&lt;p&gt;Test your knowledge of our prices.&lt;/p&gt;', kind=None),
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
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='How much do we sell our Cable Management Box?', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value='simple_choice', kind=None),
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
                                                                                            Constant(value='$20', kind=None),
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
                                                                                            Constant(value='$50', kind=None),
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
                                                                                            Constant(value='$80', kind=None),
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
                                                                                            Constant(value='is_correct', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='$100', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                            Constant(value=True, kind=None),
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
                                                                                            Constant(value='$200', kind=None),
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
                                                                                            Constant(value='$300', kind=None),
                                                                                            Constant(value=6, kind=None),
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
                                                                    Constant(value='column_nb', kind=None),
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Select all the products that sell for $100 or more', kind=None),
                                                                    Constant(value=9, kind=None),
                                                                    Constant(value='multiple_choice', kind=None),
                                                                    Constant(value='2', kind=None),
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
                                                                                            Constant(value='answer_score', kind=None),
                                                                                            Constant(value='is_correct', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Corner Desk Right Sit', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                            Constant(value=1, kind=None),
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
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                            Constant(value='is_correct', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Desk Combination', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                            Constant(value=1, kind=None),
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
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Cabinet with Doors', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
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
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                            Constant(value='is_correct', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Large Desk', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                            Constant(value=1, kind=None),
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
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Letter Tray', kind=None),
                                                                                            Constant(value=5, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
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
                                                                                            Constant(value='value', kind=None),
                                                                                            Constant(value='sequence', kind=None),
                                                                                            Constant(value='answer_score', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='Office Chair Black', kind=None),
                                                                                            Constant(value=6, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
                                                                                            ),
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
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='What do you think about our prices (not rated)?', kind=None),
                                                                    Constant(value=10, kind=None),
                                                                    Constant(value='simple_choice', kind=None),
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
                                                                                            Constant(value='Very underpriced', kind=None),
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
                                                                                            Constant(value='Underpriced', kind=None),
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
                                                                                            Constant(value='Correctly priced', kind=None),
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
                                                                                            Constant(value='A little bit overpriced', kind=None),
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
                                                                                            Constant(value='A lot overpriced', kind=None),
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
                                                                    Constant(value='is_page', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='description', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Policies', kind=None),
                                                                    Constant(value=11, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value='&lt;p&gt;Test your knowledge of our policies.&lt;/p&gt;', kind=None),
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
                                                                    Constant(value='is_scored_question', kind=None),
                                                                    Constant(value='answer_numerical_box', kind=None),
                                                                    Constant(value='answer_score', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='How many days is our money-back guarantee?', kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='numerical_box', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=30, kind=None),
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
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='is_scored_question', kind=None),
                                                                    Constant(value='answer_date', kind=None),
                                                                    Constant(value='answer_score', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='If a customer purchases a product on 6 January 2020, what is the latest day we expect to ship it?', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value='2020-01-08', kind=None),
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
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                    Constant(value='is_scored_question', kind=None),
                                                                    Constant(value='answer_datetime', kind=None),
                                                                    Constant(value='answer_score', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='If a customer purchases a 1 year warranty on 6 January 2020, when do we expect the warranty to expire?', kind=None),
                                                                    Constant(value=14, kind=None),
                                                                    Constant(value='datetime', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value='2021-01-07 00:00:01', kind=None),
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
                                                                    Constant(value='title', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='question_type', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='What day to you think is best for us to start having an annual sale (not rated)?', kind=None),
                                                                    Constant(value=15, kind=None),
                                                                    Constant(value='date', kind=None),
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
                                                                ],
                                                                values=[
                                                                    Constant(value='What day and time do you think most customers are most likely to call customer service (not rated)?', kind=None),
                                                                    Constant(value=16, kind=None),
                                                                    Constant(value='datetime', kind=None),
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
                                                                ],
                                                                values=[
                                                                    Constant(value='How many chairs do you think we should aim to sell in a year (not rated)?', kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='numerical_box', kind=None),
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
                    name='test_04_certification_success_tour',
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
                                    attr='survey_certification',
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
                                    Constant(value='test_certification_success', kind=None),
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
                    name='test_05_certification_failure_tour',
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
                                    attr='survey_certification',
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
                                    Constant(value='test_certification_failure', kind=None),
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
