import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests

# ============================================================================
# APP CONFIGURATION (Must be the first command)
# ============================================================================
st.set_page_config(
    page_title="BYU Accounting Study App",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "🏠 Home"

if 'chat_history_402' not in st.session_state:
    st.session_state.chat_history_402 = []

# ============================================================================
# FULL TEXTBOOK CONTENT FOR AI REFERENCE
# ============================================================================
FULL_TEXTBOOK_CONTENT = """
=== COMPLETE TEXTBOOK CONTENT FOR ACC 402 ===

CHAPTER 1: MANAGEMENT ACCOUNTING AND COST MANAGEMENT

Management Accounting and the Role of Cost Management

Management accountants are the accounting and finance professionals who develop and use cost management information to assist in implementing the organization's strategy. Cost management information consists of financial information about costs and revenues and nonfinancial information about customer retention, productivity, quality, and other key success factors for the organization. Cost management is the development and use of cost management information.

The strategic role of the management accountant in an organization is explained in the definition of management accounting provided by the Institute of Management Accountants (IMA):

Management accounting is a profession that involves partnering in management decision making, devising planning and performance management systems, and providing expertise in financial reporting and control to assist management in the formulation and implementation of an organization's strategy.

Management accountants use their unique expertise (decision making, planning, performance management, and more), working with the organization's managers, to help the organization succeed in formulating and implementing its strategy. Cost management information is developed and used within the organization's information value chain, from stage 1 through stage 5.

At lower stages of the value chain, management accountants gather and summarize data (stage 2) from business events (stage 1) and then transform the data into cost management information (stage 3) through analysis and use of the management accountants' expertise. At stage 4, cost management information is combined with other information about the organization's strategy and competitive environment to produce actionable knowledge. At stage 5, management accountants use this knowledge to participate with management teams in making decisions that advance the organization's strategy.

The Four Functions of Management

The management accountant develops cost management information for the CFO, other managers, and employee teams to use to manage the firm and make the firm more competitive and successful. Cost management information is provided for each of the four major management functions:

1. Strategic management
2. Planning and decision making
3. Management and operational control
4. Preparation of financial statements

The most important function is strategic management, which is the development and implementation of a sustainable competitive position in which the firm's competitive advantage provides continued success. A strategy is a set of goals and specific action plans that, if achieved, provide the desired competitive advantage. Strategic management involves identifying and implementing these goals and action plans.

Strategic Management. Cost management information is needed to make sound strategic decisions regarding choice of products, manufacturing methods, marketing techniques and distribution channels, customer profitability, and other long-term issues.

Planning and Decision Making. Cost management information is needed to support recurring decisions regarding replacing equipment, managing cash flow, budgeting materials purchases, scheduling production, and pricing.

Management and Operational Control. Cost management information is needed to provide a fair and effective basis for identifying inefficient operations and to reward and motivate effective managers.

Preparation of Financial Statements. Cost management information is needed to provide accurate accounting for inventory and other assets, in compliance with reporting requirements, for the preparation of financial reports and for use in the three other management functions.

The third area of responsibility, control, consists of two functions, operational control and management control. Operational control takes place when mid-level managers (e.g., site managers, product managers, regional managers) monitor the activities of operating-level managers and employees (e.g., production supervisors and various department heads). In contrast, management control is the evaluation of mid-level managers by upper-level managers (the controller or the CFO).

In the fourth function, preparation of financial statements, management complies with the reporting requirements of relevant groups (such as the Financial Accounting Standards Board) and relevant federal government authorities (e.g., the Internal Revenue Service and the Securities and Exchange Commission).

Strategic Management and the Strategic Emphasis in Cost Management

Effective strategic management is critical to the success of the firm and is a pervasive theme of this book. The growing pressures of economic recession, global competition, technological innovation, and changes in business processes have made cost management more critical and dynamic than ever before. Managers must think competitively; doing so requires a strategy.

Strategic thinking involves anticipating changes; products, services, and operating processes are designed to accommodate expected changes in customer demands. Flexibility is important. The ability to make fast changes is critical as a result of the demands of new concepts such as e-commerce, speed-to-market, and flexible manufacturing.

The strategic emphasis also requires creative and integrative thinking, that is, the ability to identify and solve problems from a cross-functional view. The business functions are often identified as marketing, production, finance, and accounting/controllership. Instead of viewing a problem as a production problem, a marketing problem, or a finance and accounting problem, cross-functional teams view it using an integrative approach that combines skills from all functions simultaneously.

The Contemporary Business Environment

Cost management practices often need to adjust in response to changes in the contemporary business environment. Some of the changes in recent years include:

1. Growth in global competition
2. Lean manufacturing
3. Advances in information technologies and enterprise resource management
4. Continued focus on the customer
5. New forms of management organization
6. Changes in the social, political, and cultural environment of business, including the impact of climate change

The Global Business Environment

A key development that drives change in the contemporary business environment is the growth of international markets and trade due to the rise of economies throughout the world and the decline of trade barriers in many countries.

Lean Manufacturing

To remain competitive in the face of the increased global competition, firms around the world are adopting new manufacturing technologies. These include just-in-time inventory methods to reduce the cost and waste of maintaining large levels of materials and unfinished product. Also, many firms are adopting the lean methods applied in Japanese manufacturing that have produced significant cost and quality improvements through the use of quality teams and statistical quality control.

Use of Information Technology, the Internet, and Enterprise Resource Management

Perhaps the most fundamental of all business changes has been the increasing use of information technology, the internet, and other technologies such as blockchain and artificial intelligence. This new economy is reflected in the rapid growth of internet-based firms; the increased use of the internet for communications, sales, and business data processing; and the use of enterprise management systems.

Focus on the Customer

A key element in the business environment is the need to meet high consumer expectation for product functionality and quality. To meet this expectation, companies have adopted shorter product life cycles, to add new features and new products as quickly as possible, thereby increasing the overall intensity of competition.

Management Organization

Management organization is changing in response to the changes in technology, marketing, and manufacturing processes. Because of the focus on customer satisfaction and value, the emphasis has shifted from financial and profit-based measures of performance to customer-related, nonfinancial performance measures such as quality, time to delivery, and service.

Environmental, Social, and Governance (ESG) Considerations

An additional change to the business environment is an increased concern for how companies manage their relationships with the world in which they operate. Specifically, investors and activist groups are calling on companies to provide regular information about their environmental, social, and governance (ESG) activities.

A company's environmental activities relate to its work to safeguard the environment, including policies to combat climate change. Its social activities relate to how it manages its relationships with employees, customers, and the community at large. Its governance activities relate to issues such as ethical leadership, executive pay, board composition, and shareholder rights.

Contemporary Management Techniques: The Management Accountant's Response to the Contemporary Business Environment

Management accountants, guided by a strategic focus, have responded to the six changes in the contemporary business environment with 13 methods that are useful in implementing strategy in these dynamic times.

The first six methods focus directly on strategy implementation:
1. The balanced scorecard and strategy map
2. Value chain
3. Activity-based costing and management
4. Business analytics
5. Target costing
6. Life-cycle costing

The next seven methods help to achieve strategy implementation through a focus on process improvement:
7. Benchmarking
8. Business process improvement
9. Total quality management
10. Lean accounting
11. The theory of constraints
12. Sustainability
13. Enterprise risk management

The Balanced Scorecard (BSC) and Strategy Map

Strategic information using critical success factors provides a road map for the firm to use to chart its competitive course and serves as a benchmark for competitive success. Financial measures such as profitability reflect only a partial, and frequently only a short-term, measure of the firm's progress.

To emphasize the importance of using strategic information, both financial and nonfinancial, accounting reports of a firm's performance are now often based on critical success factors in four different perspectives:

1. Financial performance. Measures of profitability and market value, among others, as indicators of how well the firm satisfies its owners and shareholders.

2. Customer satisfaction. Measures of quality, service, and low cost, among others, as indicators of how well the firm satisfies its customers.

3. Internal processes. Measures of the efficiency and effectiveness with which the firm produces the product or service.

4. Learning and growth. Measures of the firm's ability to develop and utilize human resources to meet its strategic goals now and into the future.

An accounting report based on the four perspectives is called a balanced scorecard (BSC). The concept of balance captures the intent of broad coverage, financial and nonfinancial, of all factors that contribute to the firm's success in achieving its strategic goals.

The strategy map is a diagram that links the various perspectives in a balanced scorecard. For many companies, high achievement in the learning and growth perspective contributes directly to higher achievement in the internal process perspective, which in turn causes greater achievement in the customer satisfaction perspective, which then produces the desired financial performance.

The Value Chain

The value chain is an analysis tool organizations use to identify the specific steps required to provide a competitive product or service to the customer. In particular, an analysis of the firm's value chain helps management discover which steps or activities are not competitive, where costs can be reduced, or which activity should be outsourced.

A key idea of value-chain analysis is that the firm should carefully study each step in its operations to determine how each step contributes to the firm's profits and competitiveness.

Activity-Based Costing and Management

Many firms have found that they can improve planning, product costing, operational control, and management control by using activity analysis to develop a detailed description of the specific activities performed in the firm's operations. The activity analysis provides the basis for activity-based costing and activity-based management.

Activity-based costing (ABC) is used to improve the accuracy of cost analysis by improving the tracing of costs to products or to individual customers. Activity-based management (ABM) uses activity analysis and activity-based costing to help managers improve the value of products and services and increase the organization's competitiveness.

Business Analytics

Business analytics (BA) (also called predictive analytics) is an approach to strategy implementation in which the management accountant uses data to understand and analyze business performance. Business analytics often uses statistical methods such as regression or correlation analysis to predict consumer behavior, measure customer satisfaction, or develop models for setting prices, among other uses.

Target Costing

Target costing is a method that has resulted directly from the intensely competitive markets in many industries. Target costing determines the desired cost for a product on the basis of a given competitive price, such that the product will earn a desired profit. Cost is thus determined by price.

Life-Cycle Costing

Life-cycle costing is a method used to identify and monitor the costs of a product throughout its life cycle. The life cycle consists of all steps from product design and purchase of materials to delivery and service of the finished product. The steps typically include:

1. Research and development
2. Product design, including prototyping, target costing, and testing
3. Manufacturing, inspecting, packaging, and warehousing
4. Marketing, promotion, and distribution
5. Sales and service

Benchmarking

Benchmarking is a process by which a firm identifies its critical success factors, studies the best practices of other firms (or other business units within a firm) for achieving these critical success factors, and then implements improvements in the firm's processes to match or beat the performance of those competitors.

Business Process Improvement

Business process improvement (BPI) is a management method by which managers and workers commit to a program of continuous improvement in quality and other critical success factors. Continuous improvement is very often associated with benchmarking and total quality management as firms seek to identify other firms as models to learn how to improve their critical success factors.

Total Quality Management

Total quality management (TQM) is a method by which management develops policies and practices to ensure that the firm's products and services exceed customers' expectations. This approach includes increased product functionality, reliability, durability, and serviceability.

Lean Accounting

Firms that have adopted lean manufacturing, which is one of the six key aspects of the contemporary business environment, will also typically use lean accounting. Lean accounting uses value streams to measure the financial benefits of a firm's progress in implementing lean manufacturing.

The Theory of Constraints

The theory of constraints (TOC) is a methodology that improves profitability and cycle time by identifying the bottleneck in the operation and determining the most profitable product mix given the bottleneck. TOC helps to eliminate bottlenecks—places where partially completed products tend to accumulate as they wait to be processed in the production process.

Sustainability

Sustainability means the balancing of the organization's short- and long-term goals in all three dimensions of performance—social, environmental, and financial. We view it in the broad sense to include identifying and implementing ways to reduce cost and increase revenue as well as to maintain compliance with social and environmental regulations and expectations.

Enterprise Risk Management

Enterprise risk management (ERM) is a framework and process that organizations use to manage the risks that could negatively or positively affect the company's competitiveness and success. Risk is considered broadly to include:

1. Hazards such as fire or flood
2. Financial risks due to foreign currency fluctuations, commodity price fluctuations, and changes in interest rates
3. Operating risk related to customers, products, or employees
4. Strategic risk related to top management decisions about the firm's strategy and implementation thereof

===

CHAPTER 3: BASIC COST MANAGEMENT CONCEPTS

Costs, Cost Drivers, Cost Objects, and Cost Assignment

A critical step in achieving a competitive advantage is to identify the key costs and the drivers of those costs within the company or organization.

A company incurs a cost when it uses a resource for some purpose. Often costs are assigned into meaningful groups called cost pools. Costs can be grouped in many different ways, including by type of cost (labor costs in one pool, material costs in another), by source (department 1, department 2), or by responsibility (manager 1, manager 2).

A cost driver is any factor that has the effect of changing the amount of total cost. For a firm that competes on the basis of cost leadership, management of the key cost drivers is essential.

A cost object is any product, service, customer, activity, or organizational unit to which costs are assigned. Products, services, and customers are generally cost objects; manufacturing departments are considered either cost pools or cost objects, depending on whether management's main focus is on the costs for the products or the costs for the manufacturing departments.

Cost Assignment and Cost Allocation: Direct and Indirect Costs

Cost assignment is the process of assigning resource costs to cost pools and then from cost pools to cost objects. There are two types of assignment—direct tracing and allocation.

A direct cost can be conveniently and economically traced directly to a cost pool or a cost object. For example, the cost of materials required for a particular product is a direct cost because it can be traced directly to the product.

While tools like bar code readers and laser scanners allow for significant increases in data collection, for many organizations there is no convenient or economical way to trace an indirect cost from the cost to the cost pool or from the cost pool to the cost object. The cost of supervising manufacturing employees and the cost of handling materials are good examples of costs that generally cannot be easily or economically traced to individual products and therefore are considered indirect costs.

The assignment of indirect costs to cost pools and cost objects is called cost allocation, a form of cost assignment in which direct tracing is not economically feasible, so cost drivers are used instead. The cost drivers used to allocate or assign these costs to cost objects are often called allocation bases.

Direct and Indirect Materials Costs

Direct materials cost includes the cost of materials in the product or other cost object (less purchase discounts but including freight and related charges) and usually a reasonable allowance for scrap and defective units.

On the other hand, the cost of materials used in manufacturing that are not part of the finished product is indirect materials cost. Examples include supplies used by manufacturing employees, such as rags and small tools, or materials required by the machines, such as lubricant.

Direct and Indirect Labor Costs

Direct labor cost includes the labor used to manufacture the product or to provide the service plus some portion of non-value-added time that is normal and unavoidable, such as coffee breaks and personal time.

Indirect labor costs are labor costs associated with production, but are not direct labor. Examples include supervision, quality control, inspection, purchasing and receiving, materials handling, janitorial labor, downtime, training, and cleanup.

Other Indirect Costs

In addition to labor and materials, other types of indirect costs are necessary to manufacture the product or provide the service. They include the costs of facilities, the equipment used to manufacture the product or provide the service, and any other support equipment, such as that used for materials handling.

All indirect costs—for indirect materials, indirect labor, and other indirect items—are commonly combined into a single cost pool called overhead. In a manufacturing firm, it is often called factory overhead.

The three types of costs—direct materials, direct labor, and factory overhead—are sometimes combined for simplicity and convenience. Direct materials and direct labor are sometimes considered together and called prime costs. Similarly, direct labor and overhead are often combined into a single amount called conversion cost.

Cost Drivers and Cost Behavior

Cost drivers provide two important roles for the management accountant: (1) enabling the assignment of costs to cost objects, and (2) explaining cost behavior—that is, the change in the total amount of a cost associated with changes in the level of a cost driver.

The four types of cost drivers are activity-based, volume-based, structural, and executional.

Activity-Based Cost Drivers

Activity-based cost drivers are those factors that cause or contribute to the changes in an activity. The drivers are identified by using activity analysis—a detailed description of the specific activities performed in the firm's operations. The activity analysis includes each step in manufacturing the product or in providing the service. For each activity, a cost driver is determined to explain how the costs incurred for that activity change.

Volume-Based Cost Drivers

Many types of costs are volume-based; that is, the cost driver is the amount produced or quantity of service provided. Management accountants commonly call this volume, or volume of output, or simply output. Good examples of volume-based costs are direct materials cost and hourly direct labor cost—these costs increase with each unit of the volume of output.

The range of the cost driver in which the actual value of the cost driver is expected to fall and for which the relationship to total cost is assumed to be approximately linear is called the relevant range. Outside of this range, the relationship assumed may have to be altered.

Fixed and Variable Costs

Total cost is made up of variable costs and fixed costs. A variable cost is a cost that changes in total in response to changes in one or more cost drivers. While the cost driver can be activity-based or volume-based, typically management accountants in practice use the term variable costs in connection with volume-based cost drivers. A common example of variable costs is the cost of direct materials.

In contrast, a fixed cost is that portion of the total cost that, within the relevant range, does not change with the volume of a designated cost driver. Total fixed costs and unit variable costs are expected to remain approximately constant within the relevant range.

Fixed costs include many indirect costs, especially facility costs (depreciation, rent, insurance, taxes on the plant building), production supervisors' salaries, and other manufacturing support costs that do not change with the number of units produced.

The term mixed cost is used to refer to total cost that, within the relevant range, includes costs for both variable and fixed components.

Step Costs

A cost is said to be a step cost when it varies with the cost driver within the relevant range, but does so in steps. Step costs are characteristic of certain clerical tasks, such as order filling and claims processing.

Unit Cost

Unit cost (or average cost) is the total cost of resources consumed (materials, labor, and overhead) divided by the number of units of output. While average unit cost is a useful concept in setting prices and in evaluating product profitability, it can be subject to some misleading interpretations.

To properly interpret total average unit cost, we must distinguish unit variable costs, which do not change as output changes, from unit fixed costs, which do change as output changes.

Capacity vs. Usage of Costs

It is important to distinguish between costs that provide capacity for operations (e.g., plant building and equipment) and costs that are consumed during operations (e.g., direct materials). The former are fixed costs, while the latter are variable costs.

Structural and Executional Cost Drivers

Structural and executional cost drivers are used to facilitate strategic decision making. Structural cost drivers are strategic in nature because they involve decisions that have long-term effects on the firm's total costs.

Four examples of decisions involving structural cost drivers:

1. Scale. Larger firms have lower overall costs as a result of economies of scale.

2. Experience. Firms having employees with greater manufacturing and sales experience will likely have lower development, manufacturing, and distribution costs.

3. Technology. New technologies can reduce design, manufacturing, distribution, and customer service costs significantly.

4. Complexity. How many different products does the firm have? Firms with many products have higher costs of scheduling and managing the production process, as well as the upstream costs of product development and the downstream costs of distribution and service.

Executional cost drivers are factors the firm can manage in short-term, operational decision making to reduce costs. Here are three examples of executional cost drivers:

1. Workforce empowerment. Are the employees dedicated to continual improvement and quality? This workforce commitment will lower costs.

2. Design of the production process. Is the production process efficient? Speeding up the flow of product through the firm can reduce costs.

3. Supplier relationships. Can the cost, quality, or delivery of materials and purchased parts be improved to reduce overall costs?

Cost Concepts for Product and Service Costing

Accurate information about the cost of products and services is important in each management function: strategic management, planning and decision making, management and operational control, and financial statement preparation.

Product Costs and Period Costs

Product inventory for both manufacturing and merchandising firms is treated as an asset on their balance sheets. As long as the inventory has market value, it is considered an asset until the inventory is sold; then the cost of the inventory is transferred to the income statement as cost of goods sold.

Product costs for a manufacturing firm include only the costs necessary to complete the product at the manufacturing step in the value chain:

1. Direct materials. The materials used to manufacture the product, which become a physical part of it.

2. Direct labor. The labor used to manufacture the product.

3. Factory overhead. The indirect costs for materials, labor, and facilities used to support the manufacturing process.

Product costs for a merchandising firm include the cost to purchase the product plus the transportation costs paid by the retailer or wholesaler to get the product to the location from which it will be sold or distributed.

All other costs for managing the firm and selling the product are not product costs. They are expensed in the period in which they are incurred; for that reason, they are also called period costs. Period costs (nonproduct costs) include the selling, general, and administrative costs that are necessary for the management of the company but are not involved directly or indirectly in the manufacturing process (or, for a retailer, in the purchase of the products for resale).

Manufacturing and Merchandising Costing

The cost flows in manufacturing, retail, and service firms differ. Manufacturing companies use three inventory accounts:

1. Materials Inventory, which contains the cost of the supply of materials to be used in the manufacturing process

2. Work-in-Process Inventory, which contains all costs put into the manufacture of products that are started but not complete at the financial statement date

3. Finished Goods Inventory, which contains the cost of goods that are ready for sale

An inventory formula relates the inventory accounts, as follows:

Beginning inventory + Cost added = Cost transferred out + Ending inventory

The terms cost added and cost transferred out have different meanings, depending on which inventory account is being considered:

Materials Inventory:
- Cost added: Purchase of materials
- Cost transferred out: Cost of materials used in production

Work-in-Process Inventory:
- Cost added: (1) Cost of direct materials used, (2) Direct labor cost, (3) Overhead cost
- Cost transferred out: Cost of goods manufactured

Finished Goods Inventory:
- Cost added: Cost of goods manufactured
- Cost transferred out: Cost of goods sold

Key Formulas:

Prime Costs = Direct Materials + Direct Labor
Conversion Costs = Direct Labor + Factory Overhead
Total Product Cost = Direct Materials + Direct Labor + Factory Overhead
Cost of Goods Manufactured = Beginning WIP + Manufacturing Costs - Ending WIP
Cost of Goods Sold = Beginning FG + COGM - Ending FG

===

CHAPTER 4: JOB COSTING

Costing Systems

Costing is the process of accumulating, classifying, and assigning direct materials, direct labor, and factory overhead costs to cost objects, which most commonly are products, services, or projects.

In developing the particular costing system to fit a specific firm, the management accountant must make three choices, one for each of the three following characteristics of costing methods:

1. The cost accumulation method—job costing or process costing
2. The cost measurement method—actual, normal, or standard costing
3. The overhead application method—volume-based or activity-based

Cost Accumulation: Job or Process Costing?

Costs can be accumulated by tracing costs to a specific product or service or by accumulating costs at the department level and then allocating these costs from the departments to the products or services.

In a job costing system, the jobs consist of individual products or batches of products or services. A job costing system is appropriate when most costs incurred for the job can be readily identified with a specific product, batch of products, customer order, contract, or project.

In contrast, process costing is likely to be found in a firm that primarily produces homogeneous products or services. These firms often have continuous mass production. In this case, it is economically impractical to trace most costs to individual products.

Cost Measurement: Actual, Normal, or Standard Costing?

An actual costing system uses actual costs incurred for all product costs, including direct materials, direct labor, and factory overhead.

A normal costing system uses actual costs for direct materials and direct labor, and normal costs for factory overhead. Normal costing involves estimating a portion of overhead to be assigned to each product as it is produced.

A standard costing system uses standard costs and quantities for all three types of manufacturing costs: direct materials, direct labor, and factory overhead. Standard costs are expected costs the firm should attain.

Overhead Application under Normal Costing: Volume-Based or Activity-Based?

Volume-based product costing systems allocate overhead to products or jobs using only volume-based cost drivers, such as units produced.

Activity-based costing (ABC) systems allocate factory overhead costs to products using cause-and-effect criteria with multiple cost drivers. ABC systems use both volume-based and non-volume-based cost drivers to more accurately allocate factory overhead costs to products based on resource consumption during various activities.

The Strategic Role of Costing

To compete successfully, firms need accurate cost information, regardless of their competitive strategies. This is even more likely to be true for cost leadership firms that rely on a high level of manufacturing efficiency and quality to succeed.

Job Costing: The Cost Flows

Job costing is a costing system that accumulates costs and assigns them to specific jobs, customers, projects, or contracts. The basic supporting document (usually in electronic form) in a job costing system is the job cost sheet. It records and summarizes the costs of direct materials, direct labor, and factory overhead for a particular job.

Direct and Indirect Materials Costs

As part of the preparation for the job, the firm purchases materials that are needed for the job. These purchases include both direct materials (lumber, fabric, and other direct materials) and indirect materials (glue, nails, and other indirect materials).

The purchase of materials is based off the production levels and the bill of materials for each product. The bill of materials is a detailed listing of all the materials needed for a given job.

Once production is to begin, the various production departments will refer to the bill of materials for the job and then use a materials requisition to request the materials needed for production. The materials requisition indicates the specific job charged with the materials used.

Direct and Indirect Labor Costs

Direct labor costs are recorded on the job cost sheet by means of a time ticket (an online data entry or source document) prepared for each employee. A time ticket shows the amount of time an employee worked on each job, the pay rate, and the total direct labor cost chargeable to each job.

Indirect labor costs are treated as part of the total factory overhead cost. Indirect labor includes items such as salaries or wages for supervisors, inspectors, and production warehouse clerks.

Factory Overhead Costs

Overhead application is a process of allocating factory overhead costs to cost objects. In this chapter, the cost objects are jobs. Allocation is necessary because overhead costs are not traceable to individual jobs.

Actual Costing

An actual costing system uses actual costs incurred for direct materials and direct labor and records actual factory overhead for the jobs.

Generally, the total amount of actual overhead costs is not known until the end of the accounting period when total expenses are determined. Thus, in an actual costing system, all job costs are recorded at the end of the accounting period.

Normal Costing

In practice, many firms adopt a normal costing system that uses actual costs for direct materials and direct labor and applies factory overhead to jobs by adding to the job an estimated amount of overhead in the job by using a predetermined rate.

Normal costing avoids the fluctuations in cost per unit under actual costing resulting from changes in the month-to-month volume of units produced and changes in overhead costs from month to month.

The Application of Factory Overhead in Normal Costing

The predetermined factory overhead rate is an estimated rate used to apply factory overhead cost to a specific cost object or job. The amount of overhead applied to a job using a predetermined factory overhead rate is called factory overhead applied.

The predetermined overhead rate is calculated from estimates of overhead costs and cost drivers for the upcoming operating period, usually the coming fiscal year. To obtain the predetermined overhead rate, use these four steps:

1. Estimate total factory overhead costs for the planned production for the upcoming operating period, usually a year.

2. Select the most appropriate cost driver(s) for applying the factory overhead costs.

3. Estimate the total amount of the chosen cost driver(s) for the upcoming operating period.

4. Divide the estimated factory overhead costs by the estimated amount of the chosen cost driver(s) to obtain the predetermined overhead rate.

Cost Drivers for Factory Overhead Application

The cost driver selected for applying a predetermined overhead rate can be either a volume- or activity-based cost driver. Direct labor hours, direct labor costs, and machine-hours are among the most frequently used volume-based cost drivers for applying factory overhead.

Applying Factory Overhead Costs

The predetermined overhead rate usually is calculated at the beginning of the year and is used throughout the year.

Predetermined factory overhead rate = Estimated total factory overhead amount for the year / Estimated total amount of cost driver for the year

Departmental Overhead Rates

When the production departments in the plant are very similar as to the amount of overhead in each department and the usage of cost drivers in the departments, then the use of a plantwide rate (one rate for all production departments taken as a whole) is appropriate.

In many cases, however, the various production departments differ significantly in the amount of cost or cost drivers. Using a departmental allocation approach, the rates are calculated separately for each department, and the overhead is allocated to products based on the usage of each department's resources.

Disposition of Underapplied and Overapplied Overhead

Using a predetermined factory overhead rate to apply overhead cost to products can cause total overhead applied to the units produced to exceed the actual overhead incurred in periods when production is higher than expected.

Overapplied overhead is the amount of factory overhead applied that exceeds the actual factory overhead cost incurred.

On the other hand, it is possible that applied overhead will be less than the incurred amount of overhead. Underapplied overhead is the amount by which actual factory overhead exceeds factory overhead applied.

Underapplied or overapplied overhead can be disposed of in two ways:

1. Adjust the Cost of Goods Sold account.

2. Adjust the production costs of the period; that is, allocate (often called "prorate") the underapplied or overapplied overhead among the ending balances of Work-in-Process Inventory, Finished Goods Inventory, and Cost of Goods Sold.

Adjustment to Cost of Goods Sold

When the amount of underapplied or overapplied overhead is not significant, it generally is adjusted to Cost of Goods Sold because all product costs eventually become cost of goods sold.

Proration Approach

If management believes the amount of overapplied or underapplied overhead represents a material amount, then proration of the amount to Work-in-Process Inventory, Finished Goods Inventory, and Cost of Goods Sold is the preferred method of disposal.

Potential Errors in Overhead Application

The application of overhead is a critical step in costing, and because it is based on estimates, it is subject to potential errors in determining the cost of a product or service. There are three types of potential errors:

1. Aggregation error. This costing error arises when, for example, a single plantwide rate is used instead of departmental rates.

2. Specification error. This error arises when the wrong cost driver is used in the application rate.

3. Measurement error. This is a common type of error that arises when the amounts used for estimated cost drivers or estimated overhead are incorrect.

Job Costing in Service Industries; Project Costing

Job costing is used extensively in service industries such as advertising agencies, hospitals, and repair shops, as well as consulting, architecture, accounting, and law firms. Instead of using the term job, accounting and consulting firms use the term client or project, hospitals and law firms use the term case, and advertising agencies use the term contract or project. Many firms use the term project costing to indicate the use of job costing in service industries.

Operation Costing

Operation costing is a hybrid costing system that uses a job costing approach to assign direct materials costs to jobs and a process costing approach to assign conversion costs to products or services.

Manufacturing operations whose conversion activities are very similar across several product lines, but whose direct materials used in the various products differ significantly, use operation costing.

Industries suitable for applying operation costing include food processing, textiles, shoes, furniture, metalworking, jewelry, and electronic equipment.

===

CHAPTER 6: PROCESS COSTING

Characteristics of Process Costing Systems

Firms having homogeneous products that pass through a series of similar processes or departments use process costing. These firms usually engage in continuous mass production of a few similar products. Manufacturing costs are accumulated in each process.

The process costing system is used in many industries such as chemicals, oil refining, textiles, paints, flour, canning, rubber, steel, glass, food processing, mining, electronics, plastics, drugs, paper, lumber, leather goods, metal products, and sporting goods.

Equivalent Units

An equivalent unit is the measure commonly used in process costing. Equivalent units are the number of the same or similar complete units that could have been produced given the amount of work actually performed on both complete and partially complete units.

Equivalent units are not the same as physical units. For example, suppose in a given month a chemical company had 30,000 gallons of a chemical in production, of which 20,000 gallons were complete at the end of the month but the remaining 10,000 gallons were only 50% complete. The equivalent units would be 25,000 gallons [20,000 + (10,000 × 50%)].

The equivalent units should be calculated separately for direct materials, direct labor, and factory overhead when the proportion of the total work performed on the units in the Work-in-Process Inventories is not always the same for each cost element.

Conversion Costs

Because overhead is often applied on the basis of direct labor hours, and because of the relatively small direct labor content in most process industries, factory overhead and direct labor costs are often combined and called conversion costs for the purpose of computing equivalent units of production.

Many manufacturing operations incur conversion costs uniformly throughout production. The equivalent units of conversion costs are therefore the result of multiplying the percentage of work that is complete during the period by the number of units on which work is partially complete.

Direct Materials

Direct materials can be added at discrete points or continuously during production. If the materials are added uniformly, the proportion used for computing equivalent units of direct materials is the same as the proportion for conversion costs, and a separate calculation of the direct materials per equivalent would not be necessary.

However, if the materials are added all at once, the proportion used in the computation depends on whether the point in the process where the materials are added has been reached.

Flow of Costs in Process Costing

In process costing, costs flow through different processes or departments. A separate Work-in-Process Inventory account is used to record costs of each production department.

When one department finishes its work, the costs of the goods completed are transferred to the next department's Work-in-Process Inventory account for further work. After this further work, the costs of goods completed are then transferred to the Finished Goods Inventory account.

Starting with the second department, an additional cost element, transferred-in costs, appears. These are costs of the goods completed in the prior department and transferred into this department during the period.

Steps in Process Costing (The Production Cost Report)

The key document in a typical process costing system is the production cost report, prepared at the end of each period for each production process or department. The production cost report summarizes the number of physical units and equivalent units of a department, the costs incurred during the period, and the costs assigned to both units completed (and transferred out) and ending Work-in-Process Inventories.

The preparation of a production cost report includes five steps:

Step 1: Analyze the physical flow of production units.

Step 2: Calculate equivalent units for each manufacturing cost element (direct materials, direct labor, and overhead or direct materials and conversion costs).

Step 3: Determine total costs for each manufacturing cost element from step 2.

Step 4: Compute cost per equivalent unit for each manufacturing cost element from step 2.

Step 5: Assign total manufacturing costs to units completed and ending Work-in-Process (WIP).

Step 1: Analyze the Physical Flow of Production Units

The first step determines the number of units on hand in beginning Work-in-Process, the number of units started into production (or received from a prior department), the number of units completed, and the number of units in ending Work-in-Process Inventory.

Input units include beginning Work-in-Process Inventory and all units that enter a production department during an accounting period. Output units include units that are complete and transferred out from a production department and units in the ending Work-in-Process Inventory.

Step 2: Calculate Equivalent Units for Each Manufacturing Cost Element

The purpose of calculating equivalent units of production for each manufacturing cost element (direct materials, direct labor, and factory overhead) is to measure the total work expended on production during an accounting period. The partially complete physical units are converted into the equivalent number of whole units.

Step 3: Determine Total Costs for Each Manufacturing Cost Element

The total manufacturing costs for each cost element (direct materials, direct labor, and overhead) include the current costs incurred and the prior period costs of the units in Work-in-Process beginning inventory. The total manufacturing cost for each cost element is also called total costs to account for.

Step 4: Compute Cost per Equivalent Unit for Each Manufacturing Cost Element

The purpose of computing cost per equivalent unit of production is to have a proper product costing for income determination and other management needs for an accounting period, which includes both complete and incomplete units.

Step 5: Assign Total Manufacturing Costs to Units Completed and Ending WIP

The objective of the production cost report is to assign total manufacturing costs incurred to the units completed during the period and the units that are still in process at the end of the period. The total costs assigned in step 5 should equal the total costs to be accounted for in step 3.

Process Costing Methods

The two methods used to prepare the departmental production cost report when the firm uses process costing are the weighted-average method and the first-in, first-out (FIFO) method.

Weighted-Average Method

The weighted-average method includes all costs in calculating the unit cost, including both costs incurred during the current period and costs incurred in the prior period that are shown as the beginning Work-in-Process Inventory of the current period. In this method, prior period costs and current period costs are averaged—hence the name, weighted-average.

The weighted-average method makes no distinction between the cost incurred prior to the current period and the cost incurred during the current period. As long as a cost is on the current period's cost sheet for a production department, it is treated as any other cost regardless of when it was incurred.

The weighted-average method computes the total equivalent units produced to date. The number of units in production in the current period for each manufacturing production element includes both (1) the units from previous periods that are still in production at the beginning of the current period and (2) the units placed into production in the current period.

Total equivalent units = Completed and transferred out units + Ending Work-in-Process equivalent units

FIFO Method

The FIFO method includes only costs incurred and work performed during the current period in calculating the unit cost. FIFO considers the beginning inventory as a batch of goods separate from the goods started and completed within the current period. FIFO assumes that the first work done is to complete the beginning Work-in-Process Inventory.

The FIFO method does not combine beginning inventory costs with current costs when computing equivalent unit costs. While the costs from each period are treated separately, we still follow the same five steps as in the weighted-average method in determining product costs.

The equivalent units in the beginning Work-in-Process—work done in the prior period—are not counted as part of the FIFO method equivalent units. Only the equivalent units of the beginning Work-in-Process to be completed this period are counted.

FIFO equivalent units = Completed and transferred out units + Ending Work-in-Process equivalent units - Beginning Work-in-Process equivalent units

Comparison of Weighted-Average and FIFO Methods

Both the weighted-average and the FIFO methods produce the same total costs accounted for. The key difference between the two methods is the handling of partially completed beginning Work-in-Process Inventory units.

The FIFO method separates the units in the beginning inventory from the units started and completed during the period. In contrast, the weighted-average method makes no separate treatment of the units in the beginning Work-in-Process Inventory.

The weighted-average method generally is easier to use because the calculations are simpler. This method is most appropriate when Work-in-Process Inventory is relatively small or when direct materials prices and conversion costs are stable.

The FIFO method is most appropriate when direct materials prices, conversion costs, or inventory levels fluctuate significantly.

Some firms prefer the FIFO method over the weighted-average method for purposes of cost control and performance evaluation because the cost per equivalent unit under FIFO represents the cost for the current period's efforts only.

Process Costing with Multiple Departments

Most manufacturing firms have multiple departments or use several processes that require a number of steps. As the product passes from one department to another, the cost passes from department to department. The costs from the prior department are called transferred-in costs or prior department costs.

Transferred-in Costs

Transferred-in costs are costs of work performed in the earlier departments that are transferred into the present department. Including these costs is a necessary part of process costing because we treat each department as a separate entity, and each department's production cost report includes all costs added to the product up to that point.

The equivalent units of the transferred-in cost for ending Work-in-Process Inventory is always assumed to be the same as the number of units in ending Work-in-Process Inventory. Because all units in process are complete for the prior departments' costs, by definition the number of equivalent units transferred in is the same as the number of physical units transferred in.

Journal Entries for Process Costing

Process costing uses the same general ledger manufacturing accounts as job costing. However, instead of assigning product costs to specific jobs, we accumulate costs in production departments. Each department has a separate Work-in-Process Inventory account.

Implementation and Enhancement of Process Costing

Activity-Based Costing and the Theory of Constraints

Process costing systems are appropriate where there are one or a few homogeneous products. But sometimes the process-based manufacturer has very different products going through different processes, making the process costing system by itself inadequate.

Activity-based costing is an important enhancement to process costing when product and process variety arises. Similarly, process costing information is not intended to help the firm determine the most profitable product mix or to identify the most profitable use of the plant. These questions require analyses that utilize the products' contribution margins and the location of production constraints in the plant.

Just-in-Time Systems and Backflush Costing

Firms use the just-in-time (JIT) method to minimize inventory and improve quality by carefully coordinating the receipt of materials and the delivery of products with the manufacturing processes in the plant. The goal is to have little or no Direct Materials, Work-in-Process, or Finished Goods Inventory in the plant.

Because inventory is minimal in an effective JIT system, there is no need for a system such as process costing to determine equivalent units and to account for production costs in Work-in-Process and Finished Goods. Simpler methods such as backflush costing can be used instead.

Backflush costing charges current production costs (using standard unit costs) directly to finished goods inventory, without accounting for the flows in and out of the Work-in-Process account, or directly to Cost of Goods Sold without accounting for the flows in and out of WIP or Finished Goods.

Normal and Standard Process Costing

Process cost reports can take a normal costing approach; that is, direct labor and direct materials are added to product at actual cost and overhead is determined and applied to product using a predetermined overhead rate. An alternative approach is standard costing, in which all three cost elements—direct materials, direct labor, and overhead—are added to product at a standard cost rather than actual cost.

Both job costing and process costing can be applied using either the normal costing or the standard costing approach. Similarly, a process costing system can be either a traditional or an activity-based system.

===

CHAPTER 7: COST ALLOCATION: DEPARTMENTS, JOINT PRODUCTS, AND BY-PRODUCTS

The Strategic Role and Objectives of Cost Allocation

The strategic role of cost allocation has four objectives:

1. Determine accurate departmental and product costs as a basis for the evaluation of the cost efficiency of departments and the profitability of different products, financial reporting, and tax compliance.

2. Motivate managers to exert a high level of effort to achieve the goals of top management.

3. Provide the right incentive for managers to make decisions that are consistent with the goals of top management.

4. Fairly determine the rewards earned by the managers for their effort and skill and for the effectiveness of their decision making.

The first and most important objective requires the cost allocation method to be sufficiently accurate to support effective management decision making about products and departments. The cost allocation methods must also comply with the financial reporting standards of the Financial Accounting Standards Board (FASB) and the Internal Revenue Service.

The second objective, motivating managers, means that to be effective, the cost allocation (when it is later used as part of performance evaluation and compensation) must reward department managers for reducing costs as desired.

The third objective, providing the incentive for decision making, is achieved when cost allocation effectively provides the incentives for the individual manager to act autonomously in a manner that is consistent with top management's goals.

The fourth objective, fairness, is met when the cost allocation is clear and consistently applied in determining the manager's performance evaluation and compensation. The most clear and unbiased basis for cost allocation exists when a cause-and-effect relationship can be determined.

In some situations, cause-and-effect bases are not available and alternative concepts of fairness are used. One such concept is ability-to-bear, which is commonly employed with bases related to size, such as total sales, total assets, or the profitability of the user departments. Other concepts of fairness are based on equity perceived in the circumstance, such as benefit received.

The Ethical Issues of Cost Allocation

A number of ethical issues are important in cost allocation:

1. Ethical issues arise when costs are allocated to products or services that are produced for both a competitive market and a public agency or government department.

2. A second ethical issue in implementing cost allocation methods is the equity or fair share issue that arises when a governmental unit reimburses the costs of a private institution or when it provides a service for a fee to the public.

3. A third important ethical issue is the effect of the chosen allocation method on the costs of products or services sold to or from foreign subsidiaries.

Cost Allocation to Service and Production Departments

The departmental cost allocation method has three phases (or "steps"):

Phase 1: Trace, rather than allocate, all direct manufacturing costs and allocate manufacturing overhead costs to both the service departments and the production departments

Phase 2: Allocate the service department costs to the production departments

Phase 3: Allocate the production department costs to the products

First Phase: Trace Direct Costs and Allocate Indirect Costs to All Departments

The first phase in the departmental allocation approach traces the direct costs and allocates the indirect manufacturing costs in the plant to each service and production department.

Direct manufacturing costs are wages and materials that can be directly linked or traced to a department; for example, direct materials and direct labor costs would be traced to the production departments where they are used. Indirect costs, such as indirect materials, indirect labor, and other costs that cannot be easily and economically traced to a department are allocated by means of a predetermined cost driver to the departments that use those resources.

Allocation in Second and Third Phases

The second phase allocates service department costs to the production departments. This is the most complex of the allocation phases because services can flow back and forth between the service departments. These are often called reciprocal flows, which represent the flow of services back and forth between service departments.

Management accountants can choose among three common methods to allocate costs for the second phase:
1. The direct method
2. The step method
3. The reciprocal method

The Direct Method

The direct method of departmental cost allocation is the simplest of the three methods because it ignores the reciprocal flows. The cost allocation is accomplished by using the service flows only to production departments and determining each production department's share of that service.

The Step Method

The second method to allocate service department costs is the step method, so-called because it uses a sequence of steps in allocating service department costs to production departments. In the first step, one service department is selected to be allocated fully, that is, to allocate its costs to the other service departments as well as to each production department.

The department to be allocated first usually is chosen because it provides the highest percentage of service to other service departments. Overall, this means that the step method may provide more accurate allocations because one of the reciprocal flows between the two service departments (the one in the first step) is considered in the allocation—unlike the direct method, which ignores all reciprocal flows.

The Reciprocal Method

The reciprocal method is the preferred of the three methods because, unlike the others, it considers all reciprocal flows among the service departments. This is accomplished by using simultaneous equations; the reciprocal flows are simultaneously determined in a system of equations.

An equation for each service department represents the cost to be allocated, consisting of the first-phase allocation costs plus the cost allocated from the other department.

Implementation Issues

The key implementation issue is the choice of the most accurate allocation method. When significant differences exist, a management accountant should consider the value of the reciprocal method, which is more complete and accurate than the others because it fully considers the reciprocal flows between service departments.

Three additional issues to consider when implementing the departmental allocation approach are:

1. Disincentive effects when the allocation base is unrelated to usage
2. Disincentive effects when the allocation base is actual usage
3. Disincentive effects when allocated costs exceed external purchase cost

Disincentive Effects When the Allocation Base Is Unrelated to Usage

Determining an appropriate allocation base and the percentage amount for service provided by the service departments is often difficult. Using an inappropriate allocation base can have undesirable motivational consequences.

Disincentive Effects When the Allocation Base Is Actual Usage

When the cost allocation base is determined from actual usage, disincentives can arise because the usage of the resource by one department will affect the cost allocation to other departments.

Dual Allocation

The disincentives can be resolved by using dual allocation. Dual allocation separates fixed and variable costs and traces variable costs to the departments based on actual usage; fixed costs are allocated based on either an equal share among departments or a predetermined budgeted proportion.

The reason for the equal-share approach is that each department pays in effect a fee for the right to receive future services from the service department, irrespective of the amount of service to be used. This concept is similar to the minimum monthly charge on a checking account or for a utility bill.

Disincentive Effects When Allocated Costs Exceed External Purchase Cost

Another limitation of the three departmental allocation methods is that sometimes they can allocate a higher cost for the service than the department would pay were it to purchase the service from an outside supplier. To motivate managers to be efficient and for fairness, the allocation should be based on the cost of obtaining the service outside the firm.

Cost Allocation in Service Industries

The concepts presented in this chapter apply equally well to manufacturing, service, or not-for-profit organizations that incur joint costs. Financial institutions such as commercial banks also use cost allocation.

A service department is a unit of the organization that performs one or more support tasks for production departments by supplying engineering services, information technology, quality control, human resources management, or some other service to the production departments. The production departments assemble and finish the products.

The service department costs are allocated to the production departments, and then the costs of the production departments are allocated to the products.

Joint Product Costing

Many manufacturing plants yield more than one product from a joint manufacturing process. A joint production process is one that yields multiple outputs from a common resource input.

Joint products are products from a joint production process that have relatively substantial sales values. Products whose total sales values are minor in comparison to the sales value of the joint products are classified as by-products.

The point in a joint production process at which individual products can be separately identified for the first time is called the split-off point. Thereafter, separate production processes can be applied to the individual products.

Joint costs include all manufacturing costs incurred prior to the split-off point (including direct materials, direct labor, and factory overhead). For financial reporting purposes, these costs are allocated among the joint products.

Additional costs incurred after the split-off point that can be identified directly with individual products are called separable processing costs.

Methods for Allocating Joint Costs to Joint Products

Joint costs are most frequently allocated to joint products using:
1. The physical measure
2. The sales value at split-off
3. The net realizable value
4. The constant gross margin percentage methods

The Physical Measure Method

The physical measure method uses a physical measure such as pounds, gallons, yards, or units produced at the split-off point to allocate the joint costs to joint products.

Advantages and Limitations:
- Advantages: (1) It is easy to use and (2) the criterion for the allocation of the joint costs is objective.
- Limitations: This method ignores the revenue-producing capability of individual products that can vary widely among the joint products and have no relationship at all to any physical measure.

The Sales Value at Split-Off Method

The sales value at split-off method (or, more simply, relative sales value method) allocates joint costs to joint products on the basis of their relative sales values at the split-off point. This method can be used only when joint products can be sold at the split-off point.

Advantages and Limitations:
- Advantages: (1) It is easy to calculate and (2) is allocated according to each product's revenues. This method is superior to the physical measure method because it allocates the joint costs in proportion to the products' ability to absorb these costs.
- Limitations: One limitation is that market prices for some industries change constantly. Also, the sales price at split-off might not be available because separable processing is necessary before the product can be sold.

The Net Realizable Value Method

Not all joint products can be sold at the split-off point; some require additional processing before the product can be sold. Thus, there is no market price to attach to some products at the split-off point. In these cases, the concept of net realizable value is used.

The net realizable value (NRV) of a product is the ultimate net sales value that is estimated at the split-off point; it is determined by subtracting the separable processing and selling costs beyond the split-off point from the estimated ultimate sales value for that product.

NRV = Estimated ultimate sales value - Separable processing and selling costs

Advantages and Limitations:
The NRV method is superior to the physical measure method because, like the sales value at split-off method, it produces an allocation that yields a predictable, comparable level of profitability among the products.

The Decision to Sell before or after Additional Processing:
An important decision for management to make in regard to separable costs is whether the company should incur the separable costs and process the product further. The key to making this decision is to ignore the joint costs and focus instead on only the separable costs and the increase in sales value.

The joint costs are not relevant for the decision because these costs will not differ between the option to sell at the split-off point or to sell after additional processing.

The Constant Gross Margin Percentage Method

Sometimes it is desirable that the company has joint products with constant or equal gross margin percentages. The constant gross margin percentage method determines an allocation of joint costs so that, after allocation, all joint products have the same gross margin percentage.

The method for achieving constant gross margin percentages for joint products involves:
1. Summarizing basic data
2. Determining gross margin percent for total sales
3. Allocating joint cost and determining total product cost
4. Calculating gross margin

===

END OF TEXTBOOK CONTENT
"""
# ============================================================================
# CUSTOM CSS - DARK MODE THEME
# ============================================================================
st.markdown("""
    <style>
    /* ===== GLOBAL STYLES ===== */
    /* Force dark background everywhere */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Make top header bar black */
    header[data-testid="stHeader"] {
        background-color: #0E1117 !important;
    }
    
    /* Professional font throughout app */
    .stApp {
        font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* ===== TEXT COLORS ===== */
    /* Change all text to white for contrast */
    .stApp, .stMarkdown, p, span, div, label, li, td, th {
        color: #FFFFFF !important;
    }
    
    /* Code blocks */
    code {
        color: #FFFFFF !important;
        background-color: #1E1E1E !important;
    }
    
    .stCodeBlock, pre {
        background-color: #1E1E1E !important;
    }
    
    /* ===== SIDEBAR STYLING ===== */
    section[data-testid="stSidebar"] {
        background-color: #0E1117 !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #0E1117 !important;
    }
    
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    section[data-testid="stSidebar"] .row-widget.stRadio > div {
        background-color: #1E1E1E !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    
    section[data-testid="stSidebar"] h1 {
        color: #FFFFFF !important;
    }
    
    /* ===== ALL BUTTONS - GOLD WITH WHITE TEXT ===== */
    /* Regular buttons */
    .stButton > button {
        background-color: #CFB53B !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border: none !important;
        font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #B8A033 !important;
        color: #FFFFFF !important;
    }
    
    .stButton > button p {
        color: #FFFFFF !important;
    }
    
    /* Download buttons */
    .stDownloadButton > button {
        background-color: #CFB53B !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border: none !important;
        font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: #B8A033 !important;
        color: #FFFFFF !important;
    }
    
    .stDownloadButton > button p, .stDownloadButton > button span {
        color: #FFFFFF !important;
    }
    
    /* Form submit buttons */
    .stFormSubmitButton > button {
        background-color: #CFB53B !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
    }
    
    .stFormSubmitButton > button:hover {
        background-color: #B8A033 !important;
        color: #FFFFFF !important;
    }
    
    .stFormSubmitButton > button p {
        color: #FFFFFF !important;
    }
/* ===== EXPANDERS ===== */
    /* Expander container */
    [data-testid="stExpander"] {
        background-color: #1E1E1E !important;
        border: 1px solid #333 !important;
        border-radius: 8px !important;
    }
    
    /* Expander header - always dark background with white text */
    [data-testid="stExpander"] > details > summary {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        padding: 10px 15px !important;
    }
    
    /* Keep header dark even when expanded/focused/hovered */
    [data-testid="stExpander"] > details > summary:hover,
    [data-testid="stExpander"] > details > summary:focus,
    [data-testid="stExpander"] > details > summary:active,
    [data-testid="stExpander"] > details[open] > summary {
        background-color: #2D2D2D !important;
        color: #FFFFFF !important;
    }
    
    /* Text inside expander header */
    [data-testid="stExpander"] > details > summary p,
    [data-testid="stExpander"] > details > summary span,
    [data-testid="stExpander"] > details > summary svg {
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }
    
    /* Expander content area */
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
        background-color: #1A1A2E !important;
        border-top: 1px solid #333 !important;
        padding: 15px !important;
    }
    
    /* All text inside expander content */
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] p,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] span,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] div,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] li,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] strong,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] em {
        color: #FFFFFF !important;
    }
    
    /* Legacy expander classes for older Streamlit versions */
    .streamlit-expanderHeader {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
    }
    
    .streamlit-expanderHeader:hover,
    .streamlit-expanderHeader:focus,
    .streamlit-expanderHeader:active {
        background-color: #2D2D2D !important;
        color: #FFFFFF !important;
    }
    
    .streamlit-expanderHeader p, 
    .streamlit-expanderHeader span {
        color: #FFFFFF !important;
    }
    
    .streamlit-expanderContent {
        background-color: #1A1A2E !important;
        border: 1px solid #333 !important;
    }
    
    .streamlit-expanderContent * {
        color: #FFFFFF !important;
    }
    
    /* ===== INPUT FIELDS ===== */
    /* Text inputs */
    .stTextInput > div > div > input {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
        border-radius: 8px !important;
    }
    
    .stTextInput label {
        color: #FFFFFF !important;
    }
    
    /* Text areas - WHITE background for readability */
    .stTextArea > div > div > textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #444 !important;
        border-radius: 8px !important;
    }
    
    .stTextArea label {
        color: #FFFFFF !important;
    }
    
    /* Placeholder text in text area */
    .stTextArea > div > div > textarea::placeholder {
        color: #666666 !important;
    }
    
    /* Number inputs */
    .stNumberInput > div > div > input {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
        border-radius: 8px !important;
    }
    
    .stNumberInput label {
        color: #FFFFFF !important;
    }
    
    /* Select boxes / dropdowns */
    .stSelectbox > div > div {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
        border-radius: 8px !important;
    }
    
    .stSelectbox label {
        color: #FFFFFF !important;
    }
    
    .stSelectbox > div > div > div {
        color: #FFFFFF !important;
    }
    
    /* Dropdown menu items */
    [data-baseweb="menu"] {
        background-color: #1E1E1E !important;
    }
    
    [data-baseweb="menu"] li {
        color: #FFFFFF !important;
        background-color: #1E1E1E !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background-color: #333 !important;
    }
    
    /* ===== RADIO BUTTONS ===== */
    .stRadio > div {
        background-color: transparent !important;
    }
    
    .stRadio label {
        color: #FFFFFF !important;
    }
    
    .stRadio > div > label > div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important;
    }
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #0E1117 !important;
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border-radius: 8px 8px 0 0 !important;
        border: 1px solid #333 !important;
        padding: 10px 20px !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #2D2D2D !important;
        color: #FFFFFF !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #002E5D !important;
        color: #FFFFFF !important;
        border-bottom: 3px solid #CFB53B !important;
    }
    
    .stTabs [data-baseweb="tab-panel"] {
        background-color: #0E1117 !important;
    }
    
    /* ===== INFO/SUCCESS/WARNING/ERROR BOXES ===== */
    .stAlert {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
    }
    
    .stAlert p, .stAlert span, .stAlert div {
        color: #FFFFFF !important;
    }
    
    /* Info box */
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentInfo"]) {
        background-color: #1E3A5F !important;
        border-left: 4px solid #4A90D9 !important;
    }
    
    /* Success box */
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentSuccess"]) {
        background-color: #1E3E1E !important;
        border-left: 4px solid #4CAF50 !important;
    }
    
    /* Warning box */
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentWarning"]) {
        background-color: #3E3A1E !important;
        border-left: 4px solid #FFC107 !important;
    }
    
    /* Error box */
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentError"]) {
        background-color: #3E1E1E !important;
        border-left: 4px solid #F44336 !important;
    }
    
    /* ===== SPINNER ===== */
    .stSpinner > div {
        color: #FFFFFF !important;
    }
    
    /* ===== CAPTION TEXT ===== */
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #AAAAAA !important;
    }
    
    .stCaption p {
        color: #AAAAAA !important;
    }
    
    /* ===== CUSTOM CLASSES ===== */
    /* Course boxes styling - BLUE boxes with WHITE text */
    .course-box {
        background-color: #002E5D;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .course-box h3 {
        color: #FFFFFF !important;
        margin-bottom: 10px;
    }
    
    .course-box p {
        color: #B0B0B0 !important;
    }
    
    /* Chat message styling */
    .user-message {
        background-color: #1E3A5F;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .user-message strong, .user-message br, .user-message * {
        color: #FFFFFF !important;
    }
    
    .ai-message {
        background-color: #2D2D2D;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #CFB53B;
    }
    
    .ai-message strong, .ai-message * {
        color: #FFFFFF !important;
    }
    
    /* ===== PLOTLY CHARTS ===== */
    .js-plotly-plot .plotly .modebar {
        background-color: transparent !important;
    }
    
    .js-plotly-plot .plotly .modebar-btn path {
        fill: #FFFFFF !important;
    }
    
    /* ===== HORIZONTAL RULE ===== */
    hr {
        border-color: #333 !important;
    }
    
    /* ===== LINKS ===== */
    a {
        color: #CFB53B !important;
    }
    
    a:hover {
        color: #E8D066 !important;
    }
    
    /* ===== SCROLLBAR STYLING ===== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1E1E1E;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #444;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    
    /* ===== MARKDOWN SPECIFIC ===== */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #FFFFFF !important;
    }
    
    /* ===== TABLES ===== */
    .stTable {
        background-color: #1E1E1E !important;
    }
    
    .stTable th {
        background-color: #002E5D !important;
        color: #FFFFFF !important;
    }
    
    .stTable td {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
    }
    
    /* Dataframe styling */
    [data-testid="stDataFrame"] {
        background-color: #1E1E1E !important;
    }
    
    [data-testid="stDataFrame"] * {
        color: #FFFFFF !important;
        background-color: #1E1E1E !important;
    }
    
    /* ===== METRIC STYLING ===== */
    [data-testid="stMetric"] {
        background-color: #1E1E1E !important;
        padding: 15px !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stMetric"] label {
        color: #AAAAAA !important;
    }
    
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }
    
    /* ===== MULTISELECT ===== */
    .stMultiSelect > div > div {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
    }
    
    .stMultiSelect span {
        color: #FFFFFF !important;
    }
    
    /* ===== CHECKBOX ===== */
    .stCheckbox label {
        color: #FFFFFF !important;
    }
    
    .stCheckbox span {
        color: #FFFFFF !important;
    }
    
    /* ===== FILE UPLOADER ===== */
    [data-testid="stFileUploader"] {
        background-color: #1E1E1E !important;
        border: 1px dashed #444 !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stFileUploader"] * {
        color: #FFFFFF !important;
    }
    
    /* ===== SLIDER ===== */
    .stSlider label {
        color: #FFFFFF !important;
    }
    
    .stSlider [data-testid="stTickBarMin"], 
    .stSlider [data-testid="stTickBarMax"] {
        color: #FFFFFF !important;
    }
    
    /* ===== DATE/TIME INPUT ===== */
    .stDateInput > div > div > input,
    .stTimeInput > div > div > input {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
    }
    
    .stDateInput label, .stTimeInput label {
        color: #FFFFFF !important;
    }
    
    /* ===== COLUMN CONTAINER ===== */
    [data-testid="column"] {
        background-color: transparent !important;
    }
    
    /* ===== POPOVER/TOOLTIP ===== */
    [data-baseweb="popover"] {
        background-color: #1E1E1E !important;
    }
    
    [data-baseweb="popover"] * {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
with st.sidebar:
    # BYU Logo
    st.markdown("""
        <div style='text-align: center; margin-bottom: 20px;'>
            <svg width="150" height="150" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <circle cx="50" cy="50" r="45" fill="#002E5D"/>
                <text x="50" y="45" font-size="24" fill="white" text-anchor="middle" font-weight="bold" font-family="Arial">BYU</text>
                <text x="50" y="65" font-size="10" fill="white" text-anchor="middle" font-family="Arial">ACCOUNTING</text>
            </svg>
        </div>
    """, unsafe_allow_html=True)
    
    st.title("📚 Study App")
    st.markdown("---")
    
    # Navigation buttons
    pages = [
        "🏠 Home",
        "🧮 Calculators",
        "📖 Formula Database",
        "📊 Break-Even Visualizer",
        "📕 ACC 402 - Cost Accounting"
    ]
    
    for page_name in pages:
        if st.button(page_name, key=f"nav_{page_name}", use_container_width=True):
            st.session_state.selected_page = page_name
            st.rerun()
    
    st.markdown("---")
    st.markdown("**Created for BYU Accounting Students**")
    st.markdown("*Using AI & Data Analytics*")

# ============================================================================
# MAIN CONTENT AREA
# ============================================================================

page = st.session_state.selected_page

# --- PAGE 1: HOME ---
if page == "🏠 Home":
    # Centered welcome message
    st.markdown("""
        <div style='text-align: center; padding: 40px 20px;'>
            <h1 style='color: #FFFFFF; font-size: 2.5em; margin-bottom: 10px;'>
                Welcome to BYU Accounting Study App! 📚
            </h1>
            <p style='color: #B0B0B0; font-size: 1.2em; margin-top: 0;'>
                Your One-Stop Study Resource for Accounting Success
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Quick Access to Courses section
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: #FFFFFF;'>📚 Quick Access to Courses</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="course-box">
            <h3>📕 ACC 402 - Cost Accounting</h3>
            <p>AI Tutor with full textbook access • Practice problems • Formula reference</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to ACC 402", key="goto_402"):
            st.session_state.selected_page = "📕 ACC 402 - Cost Accounting"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="course-box">
            <h3>🧮 Calculators</h3>
            <p>Quick calculation tools • Break-even analysis • Overhead rates</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Calculators", key="goto_calc"):
            st.session_state.selected_page = "🧮 Calculators"
            st.rerun()

# --- PAGE 2: CALCULATORS ---
elif page == "🧮 Calculators":
    if st.button("← Back to Home", key="back_calc"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.title("🧮 Accounting Calculators")
    
    calc_type = st.selectbox(
        "Choose a calculator:",
        ["Contribution Margin", "Break-Even Point (Units)", "Break-Even Point (Dollars)", 
         "Target Profit", "Overhead Rate"]
    )
    
    st.markdown("---")
    
    if calc_type == "Contribution Margin":
        st.subheader("Contribution Margin Calculator")
        sales = st.number_input("Sales ($)", min_value=0.0, value=100000.0, step=1000.0)
        var_costs = st.number_input("Variable Costs ($)", min_value=0.0, value=60000.0, step=1000.0)
        
        if st.button("Calculate", key="cm_calc"):
            cm = sales - var_costs
            cm_ratio = (cm / sales * 100) if sales > 0 else 0
            
            st.success(f"**Contribution Margin:** ${cm:,.2f}")
            st.success(f"**CM Ratio:** {cm_ratio:.2f}%")
    
    elif calc_type == "Break-Even Point (Units)":
        st.subheader("Break-Even Point (Units)")
        fixed = st.number_input("Fixed Costs ($)", min_value=0.0, value=30000.0, step=1000.0)
        cm_unit = st.number_input("CM per Unit ($)", min_value=0.01, value=15.0, step=1.0)
        
        if st.button("Calculate", key="bep_units"):
            bep = fixed / cm_unit
            st.success(f"**Break-Even Point:** {bep:,.0f} units")
    
    elif calc_type == "Break-Even Point (Dollars)":
        st.subheader("Break-Even Point (Dollars)")
        fixed = st.number_input("Fixed Costs ($)", min_value=0.0, value=30000.0, step=1000.0)
        cm_ratio = st.number_input("CM Ratio (%)", min_value=0.01, max_value=100.0, value=40.0, step=1.0)
        
        if st.button("Calculate", key="bep_dollars"):
            bep = fixed / (cm_ratio / 100)
            st.success(f"**Break-Even Point:** ${bep:,.2f}")
    
    elif calc_type == "Target Profit":
        st.subheader("Target Profit Calculator")
        fixed = st.number_input("Fixed Costs ($)", min_value=0.0, value=30000.0, step=1000.0)
        target = st.number_input("Target Profit ($)", min_value=0.0, value=20000.0, step=1000.0)
        cm_unit = st.number_input("CM per Unit ($)", min_value=0.01, value=15.0, step=1.0)
        
        if st.button("Calculate", key="target_profit"):
            units = (fixed + target) / cm_unit
            st.success(f"**Units Needed:** {units:,.0f} units")
    
    elif calc_type == "Overhead Rate":
        st.subheader("Predetermined Overhead Rate")
        est_oh = st.number_input("Estimated Overhead ($)", min_value=0.0, value=100000.0, step=1000.0)
        est_activity = st.number_input("Estimated Activity (hours)", min_value=1.0, value=20000.0, step=100.0)
        
        if st.button("Calculate", key="oh_rate"):
            rate = est_oh / est_activity
            st.success(f"**Overhead Rate:** ${rate:.2f} per hour")

# --- PAGE 3: FORMULA DATABASE ---
elif page == "📖 Formula Database":
    if st.button("← Back to Home", key="back_formula"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.title("📖 Accounting Formula Database")
    
    search = st.text_input("🔍 Search formulas (e.g., 'contribution', 'overhead', 'cost')")
    
    formulas = {
        "Contribution Margin": "Sales - Variable Costs",
        "Contribution Margin Ratio": "Contribution Margin ÷ Sales",
        "Break-Even Point (Units)": "Fixed Costs ÷ CM per Unit",
        "Break-Even Point (Dollars)": "Fixed Costs ÷ CM Ratio",
        "Target Profit (Units)": "(Fixed Costs + Target Profit) ÷ CM per Unit",
        "Predetermined Overhead Rate": "Estimated Overhead ÷ Estimated Activity",
        "Applied Overhead": "Predetermined Rate × Actual Activity",
        "Prime Costs": "Direct Materials + Direct Labor",
        "Conversion Costs": "Direct Labor + Factory Overhead",
        "Cost of Goods Manufactured": "Beginning WIP + Manufacturing Costs - Ending WIP",
        "Cost of Goods Sold": "Beginning FG + COGM - Ending FG",
        "Equivalent Units (WA)": "Units Completed + (Ending WIP × % Complete)",
        "Equivalent Units (FIFO)": "Work to Complete Beg. WIP + Started & Completed + (Ending WIP × % Complete)"
    }
    
    st.markdown("---")
    
    if search:
        filtered = {k: v for k, v in formulas.items() if search.lower() in k.lower()}
        if filtered:
            for name, formula in filtered.items():
                with st.expander(f"🔹 {name}"):
                    st.code(formula)
        else:
            st.warning("No formulas found. Try a different search term.")
    else:
        for name, formula in formulas.items():
            with st.expander(f"🔹 {name}"):
                st.code(formula)

# --- PAGE 4: BREAK-EVEN VISUALIZER ---
elif page == "📊 Break-Even Visualizer":
    if st.button("← Back to Home", key="back_viz"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.title("📊 Break-Even Visualizer")
    
    st.markdown("**Enter your data to see the break-even chart:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        price = st.number_input("Selling Price per Unit ($)", min_value=0.01, value=50.0, step=1.0)
        var_cost = st.number_input("Variable Cost per Unit ($)", min_value=0.0, value=30.0, step=1.0)
    
    with col2:
        fixed_costs = st.number_input("Total Fixed Costs ($)", min_value=0.0, value=40000.0, step=1000.0)
        max_units = st.number_input("Max Units to Display", min_value=100, value=5000, step=100)
    
    if st.button("Generate Chart", key="gen_chart"):
        units = list(range(0, max_units + 1, 100))
        revenue = [price * u for u in units]
        total_cost = [fixed_costs + (var_cost * u) for u in units]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(x=units, y=revenue, mode='lines', name='Revenue', 
                                 line=dict(color='green', width=3)))
        fig.add_trace(go.Scatter(x=units, y=total_cost, mode='lines', name='Total Cost', 
                                 line=dict(color='red', width=3)))
        
        bep_units = fixed_costs / (price - var_cost) if price > var_cost else 0
        bep_revenue = price * bep_units
        
        fig.add_trace(go.Scatter(x=[bep_units], y=[bep_revenue], mode='markers', 
                                 name='Break-Even Point',
                                 marker=dict(color='blue', size=12)))
        
        fig.update_layout(
            title="Break-Even Analysis",
            xaxis_title="Units Sold",
            yaxis_title="Dollars ($)",
            hovermode='x unified',
            plot_bgcolor='#0E1117',
            paper_bgcolor='#0E1117',
            font=dict(color='white')
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"**Break-Even Point:** {bep_units:,.0f} units or ${bep_revenue:,.2f}")

# --- PAGE 5: ACC 402 AI TUTOR ---
elif page == "📕 ACC 402 - Cost Accounting":
    if st.button("← Back to Home", key="back_402"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.title("📕 ACC 402 - AI Tutor & Study Guide")
    
    # Swapped tab order - AI Tutor is now first/default
    tab1, tab2 = st.tabs(["🤖 AI Tutor", "📚 Key Formulas"])
    
    with tab1:
        st.write("### 🤖 Your ACC 402 AI Study Assistant")
        st.info("💡 This AI tutor has **word-for-word access** to your full textbook (Chapters 1, 3, 4, 6, and 7). Ask anything!")
        
        # Initialize trigger flag for topic/suggestion buttons
        if 'trigger_ai_call' not in st.session_state:
            st.session_state.trigger_ai_call = False
        
        # Quick Topic Buttons
        st.markdown("**📖 Quick Topics:**")
        topic_cols = st.columns(5)
        topics = [
            ("Ch 1", "Summarize the key concepts from Chapter 1 on Management Accounting"),
            ("Ch 3", "What are the key concepts from Chapter 3 on Basic Cost Management?"),
            ("Ch 4", "Explain job costing from Chapter 4"),
            ("Ch 6", "Walk me through process costing from Chapter 6"),
            ("Ch 7", "Explain cost allocation methods from Chapter 7")
        ]
        for idx, (label, question) in enumerate(topics):
            with topic_cols[idx]:
                if st.button(label, key=f"topic_{idx}", use_container_width=True):
                    st.session_state.chat_history_402.append({
                        'role': 'user',
                        'content': question
                    })
                    st.session_state.trigger_ai_call = True
                    st.rerun()
        
        st.markdown("---")
        
        # AI Settings
        with st.expander("⚙️ AI Settings"):
            model_choice = st.radio(
                "Model (Haiku is faster & cheaper, Sonnet is smarter):",
                ["claude-sonnet-4-20250514", "claude-haiku-3-5-20241022"],
                index=0,
                horizontal=True
            )
            st.caption("💡 Tip: Use Haiku for simple questions, Sonnet for complex explanations")
        
        # Display chat history with better styling
        if st.session_state.chat_history_402:
            for message in st.session_state.chat_history_402:
                if message['role'] == 'user':
                    st.markdown(f"""
                    <div class="user-message">
                        <strong>🧑‍🎓 You:</strong><br>{message['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="ai-message">
                        <strong>🤖 AI Tutor:</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(message['content'])
            st.markdown("---")
        
        # User input
        if 'waiting_for_response' not in st.session_state:
            st.session_state.waiting_for_response = False
        
        with st.form(key="question_form_402", clear_on_submit=True):
            user_question = st.text_area(
                "Ask your question:", 
                height=100,
                placeholder="Example: What is the difference between job costing and process costing?",
                disabled=st.session_state.waiting_for_response
            )
            
            col1, col2 = st.columns([1, 5])
            with col1:
                submit_button = st.form_submit_button(
                    "Send" if not st.session_state.waiting_for_response else "Thinking...", 
                    type="primary",
                    disabled=st.session_state.waiting_for_response
                )
        
        # Action buttons row
        btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 3])
        
        with btn_col1:
            if st.button("🗑️ Clear Chat", key="clear_chat_402"):
                st.session_state.chat_history_402 = []
                st.success("Chat cleared!")
                st.rerun()
        
        with btn_col2:
            # Export chat feature
            if st.session_state.chat_history_402:
                chat_export = "\n\n".join([
                    f"{'You' if m['role'] == 'user' else 'AI Tutor'}: {m['content']}" 
                    for m in st.session_state.chat_history_402
                ])
                st.download_button(
                    "📥 Export Chat",
                    chat_export,
                    file_name="acc402_study_session.txt",
                    mime="text/plain"
                )
        
        # Check if we need to trigger AI call (from button click or form submit)
        should_call_api = False
        
        # If form was submitted with a question
        if submit_button and user_question.strip():
            st.session_state.chat_history_402.append({
                'role': 'user',
                'content': user_question
            })
            should_call_api = True
        
        # If a topic/suggestion button was clicked
        if st.session_state.trigger_ai_call:
            should_call_api = True
            st.session_state.trigger_ai_call = False
        
        # Process API call
        if should_call_api and st.session_state.chat_history_402:
            # Only call if the last message is from the user (not already answered)
            if st.session_state.chat_history_402[-1]['role'] == 'user':
                try:
                    api_key = st.secrets["ANTHROPIC_API_KEY"]
                    
                    # Prepare system prompt with FULL textbook content
                    system_prompt = f"""You are the Managerial Accounting Master Tutor, a specialized AI expert designed to help a junior-level accounting student master the material in their textbook.

Your goal is to provide clear, accurate, and exam-focused guidance based strictly on the textbook data provided below.

CORE RESPONSIBILITIES:
1. Knowledge Retrieval: Use the provided textbook content as your primary source of truth
2. Concept Simplification: Use the Feynman Technique - explain simply, then provide practical examples
3. Problem Solving: For math problems, walk through solutions step-by-step
4. Exam Prep: Create practice questions when asked

FORMATTING GUIDELINES:
- Use LaTeX for formulas (e.g., $$\\text{{BEP}} = \\frac{{\\text{{Fixed Costs}}}}{{\\text{{CM per Unit}}}}$$)
- Use bolding for key terms
- Use bullet points for lists
- Use tables for comparisons
- Be professional, encouraging, and academically rigorous

INTERACTION PROTOCOLS:
- If the student is confused, ask clarifying questions
- Check their work and point out errors
- Always cite which chapter/section you're referencing

{FULL_TEXTBOOK_CONTENT}

Now answer the student's question based on this textbook content."""
                    
                    # Make API call
                    with st.spinner("🤔 Thinking..."):
                        headers = {
                            "Content-Type": "application/json",
                            "x-api-key": api_key,
                            "anthropic-version": "2023-06-01"
                        }
                        
                        # Build conversation history for API
                        api_messages = []
                        for msg in st.session_state.chat_history_402:
                            api_messages.append({
                                "role": msg['role'],
                                "content": msg['content']
                            })
                        
                        data = {
                            "model": model_choice,
                            "max_tokens": 4096,
                            "system": system_prompt,
                            "messages": api_messages
                        }
                        
                        try:
                            response = requests.post(
                                "https://api.anthropic.com/v1/messages",
                                headers=headers,
                                json=data,
                                timeout=60
                            )
                            
                            if response.status_code == 200:
                                response_data = response.json()
                                
                                # Safe extraction of AI message
                                if response_data.get('content') and len(response_data['content']) > 0:
                                    ai_message = response_data['content'][0]['text']
                                else:
                                    ai_message = "I'm sorry, I couldn't generate a response. Please try again."
                                
                                # Add AI response to history
                                st.session_state.chat_history_402.append({
                                    'role': 'assistant',
                                    'content': ai_message
                                })
                                st.rerun()
                            else:
                                st.error(f"❌ API Error: {response.status_code}")
                                st.code(response.text)
                        
                        except requests.exceptions.Timeout:
                            st.error("❌ Request timed out. Please try again.")
                        except requests.exceptions.RequestException as e:
                            st.error(f"❌ Network error: {str(e)}")
                        except Exception as e:
                            st.error(f"❌ Error calling API: {str(e)}")
                
                except KeyError:
                    st.error("⚠️ API key not found. Please add your Anthropic API key to Streamlit secrets.")
                    st.info("Add this to `.streamlit/secrets.toml`:")
                    st.code('ANTHROPIC_API_KEY = "your-key-here"')
        
        # Suggested questions
        st.markdown("---")
        st.markdown("**💡 Suggested Questions:**")
        
        suggestions = [
            "What's the difference between job costing and process costing?",
            "How do I calculate equivalent units using the FIFO method?",
            "Explain the reciprocal method of cost allocation",
            "What is the difference between variable and fixed costs?",
            "Walk me through the 5-step production cost report"
        ]
        
        cols = st.columns(2)
        for idx, suggestion in enumerate(suggestions):
            with cols[idx % 2]:
                if st.button(f"📌 {suggestion}", key=f"suggest_{idx}"):
                    st.session_state.chat_history_402.append({
                        'role': 'user',
                        'content': suggestion
                    })
                    st.session_state.trigger_ai_call = True
                    st.rerun()
    
    with tab2:
        st.write("### Key Formulas & Concepts")
        
        with st.expander("🔴 Contribution Margin", expanded=True):
            st.write("**Contribution Margin = Sales - Variable Costs**")
            st.write("*Amount available to cover fixed costs and profit*")
            st.code("Example: $100,000 - $60,000 = $40,000", language=None)
        
        with st.expander("🔴 Contribution Margin Ratio"):
            st.write("**CM Ratio = Contribution Margin / Sales**")
            st.write("*Percentage of each sales dollar available for fixed costs*")
            st.code("Example: $40,000 / $100,000 = 40%", language=None)
        
        with st.expander("🔴 Break-Even Point (Units)"):
            st.write("**BEP (Units) = Fixed Costs / CM per Unit**")
            st.write("*Number of units needed to cover all costs*")
            st.code("Example: $30,000 / $15 = 2,000 units", language=None)
        
        with st.expander("🔴 Break-Even Point (Dollars)"):
            st.write("**BEP ($) = Fixed Costs / CM Ratio**")
            st.write("*Sales dollars needed to break even*")
            st.code("Example: $30,000 / 0.40 = $75,000", language=None)
        
        with st.expander("🔴 Predetermined Overhead Rate"):
            st.write("**Rate = Estimated Overhead / Estimated Activity**")
            st.write("*Used to apply overhead to jobs*")
            st.code("Example: $100,000 / 20,000 hours = $5/hour", language=None)
        
        with st.expander("🔴 Equivalent Units (Weighted-Average)"):
            st.write("**EU = Units Completed + (Ending WIP × % Complete)**")
            st.write("*Measures work done in a period*")
            st.code("Example: 44,000 + (6,000 × 50%) = 47,000 EU", language=None)
        
        with st.expander("🔴 Cost of Goods Manufactured"):
            st.write("**COGM = Beg. WIP + Manufacturing Costs - Ending WIP**")
            st.write("*Total cost of units completed in production*")
