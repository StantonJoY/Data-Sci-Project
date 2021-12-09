Module(
    body=[
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tests', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_slides.tests.test_ui_wslides',
            names=[alias(name='TestUICommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestUi',
            bases=[Name(id='TestUICommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_course_certification_employee',
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
                            targets=[Name(id='user_demo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_demo',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_demo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='groups_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
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
                                                                    args=[Constant(value='base.group_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='215 Vine St', kind=None),
                                            Constant(value='Scranton', kind=None),
                                            Constant(value='18503', kind=None),
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
                                                    args=[Constant(value='base.state_us_39', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='+1 555-555-5555', kind=None),
                                            Constant(value='admin@yourcompany.example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cash_journal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.journal', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='code', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Cash - Test', kind=None),
                                            Constant(value='cash', kind=None),
                                            Constant(value='CASH - Test', kind=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.acquirer', kind=None),
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
                                                            Constant(value='provider', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='test', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='cash_journal', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='a_recv', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='code', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='reconcile', kind=None),
                                            Constant(value='user_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='X1012', kind=None),
                                            Constant(value='Debtors - (test)', kind=None),
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
                                                    args=[Constant(value='account.data_account_type_receivable', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[Name(id='a_pay', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='code', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='user_type_id', kind=None),
                                            Constant(value='reconcile', kind=None),
                                        ],
                                        values=[
                                            Constant(value='X1111', kind=None),
                                            Constant(value='Creditors - (test)', kind=None),
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
                                                    args=[Constant(value='account.data_account_type_payable', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Property', ctx=Store())],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Property', ctx=Load()),
                                    attr='_set_default',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='property_account_receivable_id', kind=None),
                                    Constant(value='res.partner', kind=None),
                                    Name(id='a_recv', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Property', ctx=Load()),
                                    attr='_set_default',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='property_account_payable_id', kind=None),
                                    Constant(value='res.partner', kind=None),
                                    Name(id='a_pay', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='product_course_channel_6', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='is_published', kind=None),
                                        ],
                                        values=[
                                            Constant(value='DIY Furniture Course', kind=None),
                                            Constant(value=100.0, kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='furniture_survey', ctx=Store())],
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
                                            Constant(value='is_attempts_limited', kind=None),
                                            Constant(value='attempts_limit', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='question_and_page_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Furniture Creation Certification', kind=None),
                                            Constant(value='5632a4d7-48cf-aaaa-8c52-2174d58cf50b', kind=None),
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
                                            Constant(value=True, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value='<p>Test your furniture knowledge!</p>', kind=None),
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
                                                                    Constant(value='description', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Furniture', kind=None),
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value='&lt;p&gt;Test your furniture knowledge!&lt;/p&gt', kind=None),
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
                                                                    Constant(value='What type of wood is the best for furniture?', kind=None),
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
                                                                                            Constant(value='Fir', kind=None),
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
                                                                                            Constant(value='Oak', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                            Constant(value=2.0, kind=None),
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
                                                                                            Constant(value='Ash', kind=None),
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
                                                                                            Constant(value='Beech', kind=None),
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
                                                                    Constant(value='column_nb', kind=None),
                                                                    Constant(value='suggested_answer_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Select all the furniture shown in the video', kind=None),
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
                                                                                            Constant(value='Chair', kind=None),
                                                                                            Constant(value=1, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                            Constant(value=1.0, kind=None),
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
                                                                                            Constant(value='Table', kind=None),
                                                                                            Constant(value=2, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1.0, kind=None),
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
                                                                                            Constant(value='Desk', kind=None),
                                                                                            Constant(value=3, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                            Constant(value=1.0, kind=None),
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
                                                                                            Constant(value='Shelve', kind=None),
                                                                                            Constant(value=4, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                            Constant(value=1.0, kind=None),
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
                                                                                            Constant(value='Bed', kind=None),
                                                                                            Constant(value=5, kind=None),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1.0, kind=None),
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
                                                                ],
                                                                values=[
                                                                    Constant(value='What do you think about the content of the course? (not rated)', kind=None),
                                                                    Constant(value=4, kind=None),
                                                                    Constant(value='text_box', kind=None),
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
                        Assign(
                            targets=[Name(id='slide_channel_demo_6_furn3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='slide.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='enroll', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='channel_type', kind=None),
                                            Constant(value='allow_comment', kind=None),
                                            Constant(value='promote_strategy', kind=None),
                                            Constant(value='is_published', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='create_date', kind=None),
                                            Constant(value='slide_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='DIY Furniture - TEST', kind=None),
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
                                                    args=[Constant(value='base.user_admin', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='payment', kind=None),
                                            Attribute(
                                                value=Name(id='product_course_channel_6', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='training', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='most_voted', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='So much amazing certification.', kind=None),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='Datetime', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=2, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='slide_type', kind=None),
                                                                    Constant(value='category_id', kind=None),
                                                                    Constant(value='is_published', kind=None),
                                                                    Constant(value='is_preview', kind=None),
                                                                    Constant(value='description', kind=None),
                                                                    Constant(value='survey_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='DIY Furniture Certification', kind=None),
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value='certification', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value="It's time to test your knowledge!", kind=None),
                                                                    Attribute(
                                                                        value=Name(id='furniture_survey', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/slides', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("certification_member")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.certification_member.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Attribute(
                                            value=Name(id='user_demo', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
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
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='tests', ctx=Load()),
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
